# Input Data Pipeline 만들기

[출처](https://www.tensorflow.org/guide/datasets)

학습 모델에 dataset을 feed-in하는 방법으로 placeholder를 생성하고 `feed-dict`를 사용하여 입력 flow를 생성하면 처리 속도가 매우 느리다. 이 방식이 효율이 떨어지는 가장 큰 이유는 data를 load하여 GPU로 전달하는 과정이 중간 중간 멈춰서 idle인 상태를 유발 하기 때문이다.

Tensorflow는 `tf.data` api를 통해 효율적인 데이터 입력 flow를 생성하는 방법을 제공한다.

[tf.data로 input pipeline 만들기 예제](data_pipeline_ex.md)

<br>

# 개요

## why tf.data?

`tf.data`는 단순할 뿐 아니라 재사용이 가능하고 복잡한 input pipleline도 구축할 수 있다.

예를 들어, image model의 pipleline은 분산 파일 시스템의 파일에서 데이터를 가져온 후,
각 이미지 dataset을 섞고 batch를 적용하는 것을 매우 직관적이고 쉽게 만들 수 있다.

## tf.data의 특징

- `tf.data.Dataset`는 각 요소가 하나 이상의 `tf.Tensor`를 포함하는 elements들을 갖는다.
- `tf.data.Dataset`은 변환(transformation)을 실시 할 수 있고, 변환(transformation)을 적용하면 변환된 `tf.data.Dataset`이 만들어진다.
- `tf.data.Iterator`는 dataset에서 element 들을 추출하는 편리한 방법들을 제공한다. element들을 주출할때 `Iterator.get_next()` 을 실행하면 이전에 실행되었던 element의 다음 element를 반환한다. input pipeline code와 model graph code 간에 interface역할을 한다 보면 될 것이다.

## input pipleline 구성 절차

아래에서 자세히 설명하지만, 간략하게 다음 단계로 요약할 수 있다.

1. 데이터 불러오기. 사용하려는 데이터로부터 Dataset 인스턴스를 만든다.
2. Iterator(반복자) 생성하기. 생성된 데이터를 사용해서 Iterator 인스턴스를 만들어 Dataset을 iterate시킨다.
3. 데이터 사용하기. 생성된 iterator를 사용해서 모델에 공급할 dataset으로부터 element를 가져올 수 있다.

---

# Basic Mechanism

`tf.data`를 사용하여 pipeline을 만드는 절차를 살펴보자

<br>

## tf.data.Datasets 인스턴스 생성

먼저 디스크에 위치한 일반 데이터들을 `tf.data.Datasets` 객체로 만들기 위해서는 다음의 두가지 방식이 이용된다

- 디스크로부터 직접 불러오기
- TFRecord 포맷으로 이미지와 레이블을 serialize하여 저장한후, 학습시 불러 오기

TFRecord 사용하는 방법은 [여기]를 참조하고, 본 post는 **디스크로부터 직접 불러오기** 하는 방식을 살펴본다.

**디스크로부터 직접 불러오기** 방식을 위해 다음의 두 method가 이용된다.

- `tf.data.Dataset.from_tensors_slice()`
- `tf.data.Dataset.from_generator()`

`tf.data.Dataset.from_tensor_slice()`는 image_list와 label_list와 같이 원본 이미지와 레이블 리스트를 입력으로 받아서 일정 크기로 slice하여 dataset을 생성해 주는 방식이다. (리스트를 slice하지 않고 list의 element 전체를 dataset으로 생성해주길 원한다면, `tf.data.Dataset.from_tensors()`를 사용한다. )

`tf.data.Dataset.from_generator()`는 사용자가 정의하는 generator method를 통해 입력 flow를 생성한다고 하지만, `tf.data.Dataset.from_tensor_slice()` 방식도 사용자가 generator method를 정의하고 이를 tf.py_func()를 통해 연결하면 둘의 차이점이 애매해진다.

> 참고로 데이터 불러오는 방법은 generator를 사용하는 방법 이외에도 numpy, tensor, placeholder를 이용한 다앙향 방식이 있다. 다음을 참고한다.
> [[다음]](https://cyc1am3n.github.io/2018/09/13/how-to-use-dataset-in-tensorflow.html)

<br>

---

# `tf.data.Dataset.from_tensor_slice()`를 사용하여 dataset 생성하기

다음은 `tf.data.Dataset.from_tensor_slice()`를 사용하여 input flow를 생성하는 방법을 예를 통해 설명한다.

```bash
# 참고로 예제에서는 다음 디렉토리 구조를 가정한다.
--- PYTHON_PROJECT
 +  dataset
    + images
    + labels
```

<br>

[[예제1]](input_pipeline_from_slice.py)

> import packages

```python
import tensorflow as tf
from glob import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
```

> 이미지 파일 및 레이블 경로

```python
image_path = 'dataset/images/'
label_path = 'dataset/labels/'
```

> input image transformation configuration

```python
resize = True
num_epoch = 1   # 0 for repeat forever
shuffle = True
batch_size = 2
```

> utility function methods

```python
def read_image(path):
    image = np.array(Image.open(path))
    return image


def _read_py_function(path, label):
    image = read_image(path)
    # image = cv2.imread(path) # OpenCV로 입력 받으는 경우
    return image.astype(np.int32), label


def _resize_function(image_decoded, label):
    image_decoded.set_shape([None, None, None])
    image_resized = tf.image.resize_images(image_decoded, [100, 100])
    return image_resized, label


def get_list(im_path, label_path):
    image_list = glob(im_path + '*.*')
    label_list = glob(label_path + '*.*')
    a = [label.split('.')[0] for label in label_list]
    label = [_a.split('/')[2] for _a in a]
    label = np.array(label).astype(np.uint8)
    return image_list, label
```

> main module

```python
def main():
    image_list, label_list = get_list(image_path, label_path)
    print('Image List: {}'.format(image_list))
    print('Label List: {}'.format(label_list))

    # tf.data.Dataset 인스턴스 생성
    dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))

    # tf.py_func를 통해 사용자 함수 _read_py_function()를 생성자로 사용
    # .map()은 생성된 인스턴스 dataset을 transformation(아래 transformation 참조)하기 위해 사용된다.
    dataset = dataset.map(
        lambda image_list, label_list: tuple(tf.py_func(_read_py_function, [image_list, label_list], [tf.int32, tf.uint8])))

    if resize:
        dataset = dataset.map(_resize_function)

    if num_epoch == 0:
        dataset = dataset.repeat() # repeat indefinately
    else:
        dataset = dataset.repeat(num_epoch)

    if shuffle:
        dataset = dataset.shuffle(buffer_size=(
            int(len(image_list) * 0.4) + 3 * batch_size))

    # .batch()도 .map()처럼 transformation method이다
    dataset = dataset.batch(batch_size)

    # Iterator 생성 (아래 Iterator 참조)
    iterator = dataset.make_initializable_iterator()
    image_stacked, label_stacked = iterator.get_next()

    with tf.Session() as sess:

        sess.run(iterator.initializer)
        while True:

            cnt += 1
            try:
                image, label = sess.run([image_stacked, label_stacked])

                image = image.astype(int)  # Convert to integer type
                jpeg_image = np.squeeze(image)

                # Plot Image for debug
                for im in jpeg_image:
                    print('Image Size: {}x{}'.format(im.shape[0], im.shape[1]))
                    plt.imshow(im)
                    plt.show()

            except tf.errors.OutOfRangeError:
                print("End of training dataset.")
                break

```

> 실행 부분

```python
if __name__ == "__main__":
    main()
```

# `tf.data.Dataset.from_generator()`를 사용하여 dataset 생성하기

`tf.data.Dataset.from_generator()`를 사용하여 dataset를 생성하는 방법도 `tf.data.Dataset.from_tensor_slices()`를 사용하는 방법과 유사하다.

예제 코드는 [[예제2]](input_pipeline_from_generator.py)를 참조한다.

---

# Transformation과 Iterator

`tf.data.Dataset` 인스턴스가 생성되며,
transformation을 사용하여 shuffle, batch등의 작업을 설정할 수 있다.

이렇게 dataset flow path가 준비되면,
Iterator를 통해 tf.Session()에 input data를 하나씩 넣어주면 된다.

Transformation과 Iterator 생성은 다음을 참조한다.

[[Datasets 변환(transformation)하기]](tf_transformation.md)

[[Iterator 생성하기]](tf_iterator.md)

> 참고로 [여기](https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html)에서는 Tensorflow Dataset pipeline을 사용한 경우와 OpenCV를 이용한 기존 pipeline 방식과의 속도 비교를 보여준다. (해당 링크의 Performance comparison 부분 참조)

---

<TO-DOs:>

상기 방식은 동일한 image사이즈에 적용된다.
Image size가 동적으로 변하면 이를 처리할 방법을 찾아야 한다.

[[Tensorflow input dataset with varying size images]](https://stackoverflow.com/questions/51983716/tensorflow-input-dataset-with-varying-size-images)

---

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
