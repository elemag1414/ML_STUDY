# Input Data Pipeline 만들기

[출처1](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)
| [출처2](<https://locslab.github.io/Tensorflow-Dataset-API(2)/>)

기존에 pipeline 생성을 위해 사용하던 방법인 데이터를 tfrecord로 변환하고서 그 파일을 학습 데이터로 넣으려고 할 때 enqueue dequeue를 이용하면 코드도 복잡하고, 여러가지 불편함들을 많았다.

tf.data를 이용하면 편리하게 tfrecord를 열 수 있는 것 뿐만이 아니라 일반 이미지도 역시 손쉽게 배치로 생성하고 넣을 수 있다.

## why tf.data?

tf.data는 단순할 뿐 아니라 재사용이 가능하고 복잡한 input pipleline도 구축할 수 있다.

예를 들어, image model의 pipleline은 분산 파일 시스템의 파일에서 데이터를 가져온 후,
각 이미지 dataset을 섞고 batch를 적용하는 것을 매우 직관적이고 쉽게 만들 수 있다.

## tf.data의 특징

- tf.data.Dataset는 각 요소가 하나 이상의 tf.Tensor를 포함하는 elements들을 갖는다.
- tf.data.Dataset은 변환(transformation)을 실시 할 수 있고, 변환(transformation)을 적용하면 변환된 tf.data.Dataset이 만들어진다.
- tf.data.Iterator는 dataset에서 element 들을 추출하는 편리한 방법들을 제공한다. element들을 주출할때 Iterator.get_next() 을 실행하면 이전에 실행되었던 element의 다음 element를 반환한다. input pipeline code와 model graph code 간에 interface역할을 한다 보면 될 것이다.

---

# Basic Mechanism

tf.data를 사용하여 pipeline을 만드는 절차를 살펴보자

## tf.data.Datasets 생성

먼저 디스크에 위치한 일반 데이터들을 tf.data.Datasets 객체로 만들기 위해서는 다음의 두가지 method가 이용된다.

- tf.data.Dataset.from_tensors()
- tf.data.Dataset.from_tensor_slice()

> 만약 저장된 데이터가 tfrecord format인 경우,
> tf.data.TFRecordDataset()를 이용하여 load 한다.
> TFRecordDataset 변환은 [여기]를 참조한다.

tf.data.Dataset.from_tensors()와 tf.data.Dataset.from_tensor_slice()의 차이점은
반환된 객체가 데이터 전체를 저장하느냐 여부이다.

다음의 예를 보자

[예제]

```python
sample = tf.random_uniform([4, 10])
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 객체 생성
dataset1 = tf.data.Dataset.from_tensors(sample)
dataset2 = tf.data.Dataset.from_tensor_slices(sample)

# 출력
print('dataset1: {}'format(dataset1))
print('dataset2: {}'.format(dataset2))
```

[결과]

```bash
dataset1: <TensorDataset shapes: (4, 10), types: tf.float32>
dataset2: <TensorSliceDataset shapes: (10,), types: tf.float32>
```

결과에서 보여지듯,
dataset1은 생성된 sample 텐서를 모두 저장하고 있고,
dataset2은 생성된 sample 텐서를 slice해서 저장하고 있다. <br>

tf.data.Dataset.from_tensor() 또는 tf.data.Dataset.from_tensor_slices()로
tf.data.Datasets객체가 만들어지면 객체안에 구성되는 element들은 동일한 구조로 구성된다.

각 element들은 tf.Tensor 형태이며 element 유형을 나타내는 tf.DType과 모양을 나타내는
tf.TensorShape로 구성된다.

<br>

또한, tf.data.Datasets로 생성되는 객체는 collection.namedtuple 또는 dictionary를
이용하여 각 구성요소를 정의 할 수 있다.

```python
# nametuples 를 이용한 구성요소 이름 지정
import collections
Sample = collections.namedtuple('sample_data', 'a b')
sample_data = Sample(
    tf.random_uniform([4]), tf.random_uniform([4, 100], maxval=100, dtype=tf.int32))
dataset = tf.data.Dataset.from_tensor_slices(sample_data)
print(dataset.output_types)     # ==> sample_data(a=tf.float32, b=tf.int32)
print(dataset.output_shapes)    # ==> sample_data(a=TensorShape([]), b=TensorShape([Dimension(100)]))
print(dataset.output_types.a)   # ==> <dtype: 'float32'>
print(dataset.output_types.b)   # ==> <dtype: 'int32'>
print(dataset.output_shapes.a)  # ==> ()
print(dataset.output_shapes.b)  # ==> (100, )


# dict 를 이용한 구성요소 이름 지정
dataset = tf.data.Dataset.from_tensor_slices(
    {
        'a': tf.random_uniform([4]),
        'b': tf.random_uniform([4, 100], maxval=100, dtype=tf.int32)
    }
)
print(dataset.output_types)     # ==> {'a' : tf.float32, 'b' : tf.int32}
print(dataset.output_shapes)    # ==> {'a': TensorShape([]), 'b': TensorShape([Dimension(100)])}
print(dataset.output_types['a'])    # ==> <dtype: 'float32'>
print(dataset.output_types['b'])    # ==> <dtype: 'int32'>
print(dataset.output_shapes['a'])   # ==> ()
print(dataset.output_shapes['b'])   # ==> (100, )
```

## Datasets 변환 (transformation)

tf.data.Datasets 객체가 생성되면 method들을 호출하여 tf.data.Datasets을 여러가지형태로 transformation 할 수 있다.

예를들어 각 요소(element) 별로도 변형이 가능 (ex. tf.data.Dataset.map()) 하고,

전체 데이터셋에 대해서도 변형이 가능하다. (ex. tf.data.Dataset.batch()).

tf.data.Datasets은 transformation과 관련된 다음과 같이 많은 method들이 있는데 해당하는 method들의 list는
해당 링크를 통해 확인한다. [[tf.data.Dataset API]](https://www.tensorflow.org/api_docs/python/tf/data/Dataset):

- [.apply(): transformation 적용](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)
- [.concatenate()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#concatenate)
- [.filter()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#filter)
- [.flat_map()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#flat_map)
- [.interleave()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
- [.map()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
- [.reduce()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#reduce)

<br>

## Iterator 생성

생성된 tf.data.Datasets의 element를 access하기 위해서는 tf.data.Iterator를 생성해야 한다.
tf.data.Iterator를 통해 각 element를 access하여 실제 값을 추출하여 model에 입력해 줘야 실제 학습이 이뤄진다.

tf.data에는 다음과 같이 총 4가지 형태의 iterator를 제공한다:

- one-shot
- initializable
- reinitializable
- feedable

각각에 대해 살펴보자

### one-shot iterator

one-shot iterator는 명시적으로 초기화 할 필요없이 한 번만 반복 할 수 있는 가장 간단한 형태의 iterator이다.
one-shot iterator는 기존 큐 기반 input pipeline이 지원하는 거의 모든 경우를 처리한다.

아래 예제를 통해 사용 방법을 살펴보자.
tf.data.Dataset.range(100)을 사용하여 0~100까지 데이터를 갖는 객체 dataset을 생성하고
make_one_shot_iterator()를 이용하여 iterator를 생성하였다.
이후 element의 access는 get_next()를 통해 다음 element를 접근한다.

> get_next()는 dunder method인 graph(next_elements)를 수행하여 다음 element를 접근한다.

```python
dataset = tf.data.Dataset.range(100)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

print(sess.run(next_element))   # ==> 0
print(sess.run(next_element))   # ==> 1
print(sess.run(next_element))   # ==> 2
print(sess.run(next_element))   # ==> 3
```

sess.run 할때마다 순차적으로 element가 출력됨을 확인 할 수 있다.

위에서 one-shot iterator는 한 번만 반복 할 수 있는 iterator라고 설명하였다.
다음 예제를 보면, while문을 사용하여 element를 출력하는 loop를 두번 반복해 보면,
실제로는 한번만 실행되는 것을 볼 수 있다.

```python
dataset = tf.data.Dataset.range(100)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

while True:
    try:
        print(sess.run(next_element), end=' ')  # ==> 0, 1, 2, 3, ..., 99
    except tf.errors.OutOfRangeError:   # 범위가 벗어나면 end를 출력하고 break
        print('end\n')
        break

while True:
    try:
        print(sess.run(next_element), end=' ') # 실행 안됨!!
    except tf.errors.OutOfRangeError:
        print('end\n')    # end 출력
        break
"""
결과 :
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 end

end
"""
```

만약 element를 출력하는 loop를 한번 더 반복하려면,
다음 예제와 같이 iterator를 다시 생성해 추가해줘야 한다.

```python
iterator2 = dataset.make_one_shot_iterator()
next_element2 = iterator2.get_next()
while True:
    try:
        print(sess.run(next_element2), end=' ')
    except tf.errors.OutOfRangeError:
        print('end')
        break
```

### initializable iterator

initializable iterator는 one-shot iterator 와 달리 작업을 시작하기 전에
명시적으로 iterator.initializer를 실행하도록 요구한다.

이 불편함을 감수하야 하지만, 대신에 다음 예제와 같이 iterator를 초기화 할때
`tf.data.Dataset’의 정의를 매개변수화 하여 사용 할 수 있다.

```python
max_value = tf.placeholder(tf.int64, shape=[])
dataset = tf.data.Dataset.range(max_value)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

# dataset의 element의 갯수를 10개로 초기화 한다.
sess.run(iterator.initializer, feed_dict={max_value: 10})
for _ in range(10):
    value = sess.run(next_element)
    print(value)               # ==> 0, 1, 2, 3, 4, .... , 9 (0부터 9까지)

# dataset의 element의 갯수를 100개로 초기화 한다.
sess.run(iterator.initializer, feed_dict={max_value: 100})
for _ in range(100):
    value = sess.run(next_element)
    print(value)                # ==> 0, 1, 2, 3, 4, .... , 100 (0부터 100까지)

```

### reinitializable iterator

reinitializable iterator는 여러가지를 초기화 할 수 있다.

예를 들어 일반화를 향상시키기 위해
입력 이미지의 랜덤으로 입력하는 train 을 위한 pipeline 과
데이터가 얼마나 정확한지 확인하는 test 를 위한 pipline은
tf.data.Dataset 의 구조가 동일하지만
서로 다른 객체를 사용해야 된다.

이때 필요한 것이 reinitializable 쉽게 처리할 수 있다.

```python
# training과 validation datasets는 같은 구조를 가진다.
training_dataset = tf.data.Dataset.range(100).map(
    lambda x: x + tf.random_uniform([], -10, 10, tf.int64))
validation_dataset = tf.data.Dataset.range(100)

# reinitializable iterator는 structure에 의해서 정의 된다.
# training_dataset 과 validation_dataset의 output_types과 output_shapes
# 속성이 호환 된다.
iterator = tf.data.Iterator.from_structure(training_dataset.output_types,
                                           training_dataset.output_shapes)
next_element = iterator.get_next()

training_init_op = iterator.make_initializer(training_dataset)
validation_init_op = iterator.make_initializer(validation_dataset)

# 20번을 반복하면서 train 과 validation 과정을 거친다.
for _ in range(20):
    # train dataset iterator를 초기화 한다.
    sess.run(training_init_op)
    for _ in range(100):
        print(sess.run(next_element))

    # validation dataset iterator를 초기화 한다.
    sess.run(validation_init_op)
    for _ in range(20):
        print(sess.run(next_element))
```

### feedable iterator

feedable iterator는 tf.placeholder를 선택하기 위해
tf.Session.run 을 통해 iterator를 전환할때 dataset의
시작부분에서 iterator를 초기화 할 필요가 없다.

```python
training_dataset = tf.data.Dataset.range(100).map(
    lambda x: x + tf.random_uniform([], -10, 10, tf.int64)).repeat()

validation_dataset = tf.data.Dataset.range(50)

# feedable iterator는 handle placeholder 와 구조로 정의된다.
# training_dataset 과 validation_dataset의 output_types과 output_shapes
# 속성이 호환 될 수 있다.
handle = tf.placeholder(tf.string, shape=[])
iterator = tf.data.Iterator.from_string_handle(
    handle, training_dataset.output_types, training_dataset.output_shapes)
next_element = iterator.get_next()

# feedable 반복자는 다양한 종류의 반복자와 함께 사용가능하다.
training_iterator = training_dataset.make_one_shot_iterator()
validation_iterator = validation_dataset.make_initializable_iterator()

# Iterator.string_handle () 메소드는 handle placeholder를 제공하기 위해
# 평가되고 사용될 수있는 텐서를 리턴한다.
training_handle = sess.run(training_iterator.string_handle())
validation_handle = sess.run(validation_iterator.string_handle())

# 20번을 반복하면서 train 과 validation 과정을 거친다.
for _ in range(20):
    for _ in range(200):
        sess.run(next_element, feed_dict={handle: training_handle})

    # Run one pass over the validation dataset.
    sess.run(validation_iterator.initializer)
    for _ in range(50):
        print(sess.run(next_element, feed_dict={handle: validation_handle}))
```

---

# tf.data로 input pipeline 만들기 예제

일반적인 input data 생성 순서는 다음과 같다:

1. 데이터의 경로를 찾는다.
2. 데이터의 목록들을 가져오고, 이미지와 레이블을 생성한다.
3. 목록의 한 열 마다 데이터를 여는 방법을 정의한다.
4. shuffle을 포함한 다양한 옵션을 설정한다.
5. 배치로 만들어서 model에 feed-in할 준비를 한다.

<br>

## 1. 데이터 준비 (경로 설정 및 이미지/레이블 생성)

제일 먼저 원하는 데이터들의 경로를 받아 리스트로 담고서 아래와 같은 함수에 넣어준다.

### <b>tf.data.TFRecordDataset(filenames)</b>

입력 데이터가 tfrecord 형태로 디스크에 저장되어 있을 경우, 이 함수를 사용하여 dataset생성한다.

### <b>tf.data.Dataset.from_tensor_slices(filenames)</b>

제일 먼저 일반 이미지나 array를 넣을 때 list 형식으로 넣어준다. 이미지 경로들이 담긴 리스트 일 수도 있고, raw 데이터의 리스트 일 수도 있다. 다음은 이 함수를 이용하는 예제이다.

```python
dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))
```

<br>

## 2. 데이터 입력 방식 정의

tfrecords가 아닌 numpy 형태나 기타의 방식(예를 들어 OpenCV로 이미지 입력받는 경우)으로
image를 읽어야 한다면 다음과 같이 preprocess 단계를 거쳐야 한다.

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

실제로 tfRecord 포맷으로 변환을 거치지 않고, PIL의 Image로 데이터를 읽어오거나 openCV로 불러오는 경우가 많다.
이럴때 앞서 preprocess 단계에서 정의한 함수를 사용하여 reader 함수를 정의 한다.

```python
dataset = dataset.map(
    lambda data_list, label_list: tuple(tf.py_func(_read_py_function, [data_list, label_list], [tf.int32, tf.uint8])))
dataset = dataset.map(_resize_function)
```

> 참고로, tensorflow api documentation에서는 코드 성능의 최적화를 위해 가능하면 tf.py_func()을 자제하도록 권한다.
> tf.py_func()는 tensorflow operation 도중에 python의 library를 사용하기 위해 쓰인다.
> 위에서 언급한 바와같이, 이 방법은 tfRecord가 아닌 다른 방식으로 image를 읽을 때 사용되는 방식으로,
> tfRecord로 변환하여 training등을 수행할때는 이 단계를 skip한다.

## 3. 데이터 입력 옵션 정의

입력 dataset을 학습시 처리하기 위해 여러 옵션을 정의할 수 있다.

- repeat(step_n) : 원하는 epoch 수를 넣을 수 있다. 아무런 파라미터를 주지 않는다면 iteration이 무한히 반복된다.
- shuffle(1000) : 각 epoch에서 dataset을 랜덤하게 섞기 위해 사용한다.

```python
dataset = dataset.repeat()
dataset = dataset.shuffle(buffer_size=(int(len(data_list) * 0.4) + 3 * batch_size))
```

## 4. batch size 설정

tf.data api가 제공되기 전까진 사용자가 batch에 대한 method를 정의하여 사용했으나, tf.data는 다음과 같이 batch() method를 제공한다.

```python
dataset = dataset.batch(batch_size)
```

## 5. iterator 생성

iterator를 생성하여 image_stacked와 label_stacked를 생성해준다.

> image_stacked와 label_stacked로 나뉘어 처리되는 이유는, 초기에 데이터 경로를
> image_list와 label_list를 tuple로 만들었기 때문에, 이후 각 tuple element별로
> 두개의 vector들이 따로 처리되어 왔기 때문이다.

```python
iterator = dataset.make_initializable_iterator()
image_stacked, label_stacked = iterator.get_next()
```

## 6. Session 수행하기

이제, tf.Session()을 생성하고 iterator를 통해 dataset을 feed-in하면
각 loop애서 처리할 image와 label이 load 된다.

아래 코드를 사용하여 input pipeline이 제대로 동작되는 확인 할 수 있다.

```python
with tf.Session() as sess:
    sess.run(iterator.initializer)
    image, label = sess.run([image_stacked, label_stacked])
```

## 최종 예제

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
