# Input Data Pipeline 만들기

[출처](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)
데이터를 tfrecord로 변환하고서 그 파일을 학습 데이터로 넣으려고 할 때 enqueue dequeue를 이용하면 코드도 복잡하고, 여러가지 불편함들을 여간 많았던 것이 아니다.

tf.data를 이용하면 편리하게 tfrecord를 열 수 있는 것 뿐만이 아니라 일반 이미지도 역시 손쉽게 배치로 생성하고 넣을 수 있다.

## tf.data로 데이터 만들기

일반적인 data 생성 순서는 다음과 같다:

1. 데이터의 경로를 찾는다.
2. 데이터의 목록들을 가져오고, 이미지와 레이블을 생성한다.
3. 목록의 한 열 마다 데이터를 여는 방법을 정의한다.
4. shuffle을 포함한 다양한 옵션을 설정한다.
5. 배치로 만들어서 model에 feed-in할 준비를 한다.

### 1. 데이터 준비 (경로 설정 및 이미지/레이블 생성)

제일 먼저 원하는 데이터들의 경로를 받아 리스트로 담고서 아래와 같은 함수에 넣어준다.

#### <b>tf.data.TFRecordDataset(filenames)</b>

이미지 파일을 tfrecord 데이터로 변환 할 때 이 함수를 사용한다.

#### <b>tf.data.Dataset.from_tensor_slices(filenames)</b>

제일 먼저 일반 이미지나 array를 넣을 때 list 형식으로 넣어준다. 이미지 경로들이 담긴 리스트 일 수도 있고, raw 데이터의 리스트 일 수도 있다. 다음은 이 함수를 이용하는 예제이다.

```python
dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))
```

<br>

### 2. 데이터 입력 방식 정의

tfrecords가 아닌 numpy 나 image를 읽어야 한다면 다음과 같이
reader 및 preprocess 함수를 정의하여 사용한다.

```python
def _read_py_function(path, label):
    image = read_image(path)
    label = np.array(label, dtype=np.uint8)
    return image.astype(np.int32), label
def _resize_function(image_decoded, label):
    image_decoded.set_shape([None, None, None])
    image_resized = tf.image.resize_images(image_decoded, [28, 28])
    return image_resized, label
```

PIL의 Image로 데이터를 불러오든 openCV로 불러오든, 이미지를 읽을 reader 함수를 정의해야 한다.  
여기에 preprocess 들을 동시에 함께 정의할 수도 있다.

```python
dataset = dataset.map(
    lambda data_list, label_list: tuple(tf.py_func(_read_py_function, [data_list, label_list], [tf.int32, tf.uint8])))
dataset = dataset.map(_resize_function)
```

> 참고로, tensorflow api documentation에서는 코드 성능의 최적화를 위해 가능하면 tf.py_func()을 자제하도록 권한다.
> tf.py_func()는 tensorflow operation 도중에 python의 library를 사용하기 위해 쓰인다.

### 3. 데이터 입력 옵션 정의

입력 dataset을 학습시 처리하기 위해 여러 옵션을 정의할 수 있다.

- repeat(step_n) : 원하는 epoch 수를 넣을 수 있다. 아무런 파라미터를 주지 않는다면 iteration이 무한히 반복된다.
- shuffle(1000) : 각 epoch에서 dataset을 랜덤하게 섞기 위해 사용한다.

```python
dataset = dataset.repeat()
dataset = dataset.shuffle(buffer_size=(int(len(data_list) * 0.4) + 3 * batch_size))
```

### 4. batch size 설정

tf.data api가 제공되기 전까진 사용자가 batch에 대한 method를 정의하여 사용했으나, tf.data는 다음과 같이 batch() method를 제공한다.

```python
dataset = dataset.batch(batch_size)
```

### 5. iterator 생성

iterator를 생성하여 image_stacked와 label_stacked를 생성해준다.

> image_stacked와 label_stacked로 나뉘어 처리되는 이유는, 초기에 데이터 경로를
> image_list와 label_list를 tuple로 만들었기 때문에, 이후 각 tuple element별로
> 두개의 vector들이 따로 처리되어 왔기 때문이다.

```python
iterator = dataset.make_initializable_iterator()
image_stacked, label_stacked = iterator.get_next()
```

### 6. Session 수행하기

이제, tf.Session()을 생성하고 iterator를 통해 dataset을 feed-in하면
각 loop애서 처리할 image와 label이 load 된다.

아래 코드를 사용하여 input pipeline이 제대로 동작되는 확인 할 수 있다.

```python
with tf.Session() as sess:
    sess.run(iterator.initializer)
    image, label = sess.run([image_stacked, label_stacked])
```

### 최종 예제

다음은 상기 내용을 이용한 최종 예제이다.

```python
import tensorflow as tf
from glob import glob


def _read_py_function(path, label):
    image = read_image(path)
    label = np.array(label, dtype=np.uint8)
    return image.astype(np.int32), label

def _resize_function(image_decoded, label):
    image_decoded.set_shape([None, None, None])
    image_resized = tf.image.resize_images(image_decoded, [28, 28])
    return image_resized, label

def onehot_encode_label(path):
    onehot_label = unique_label_names == get_label_from_path(path)
    onehot_label = onehot_label.astype(np.uint8)
    return onehot_label

# 여기서 image_list와 lable_list는 각 vector의 list이다.
# list를 사용하는 이유는 iterator를 통해 하나씩 buffer에 입력하기 위함이다.
data_list = glob('path\*.jpg') # 모든 경로들을 list로 반환
label_list = [onehot_encode_label(path).tolist() for path in data_list]
dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))
dataset = dataset.map(
    lambda data_list, label_list: tuple(tf.py_func(_read_py_function, [data_list, label_list], [tf.int32, tf.uint8])))
dataset = dataset.map(_resize_function)
dataset = dataset.repeat()
dataset = dataset.shuffle(buffer_size=(int(len(data_list) * 0.4) + 3 * batch_size))
dataset = dataset.batch(batch_size)
iterator = dataset.make_initializable_iterator()
image_stacked, label_stacked = iterator.get_next()
next_element = iterator.get_next()

# Image와 Label 확인 하기
with tf.Session() as sess:
    sess.run(iterator.initializer)
    image, label = sess.run([image_stacked, label_stacked])

```

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
