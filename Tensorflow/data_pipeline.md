# Input Data Pipeline 만들기

[출처1](https://medium.com/trackin-datalabs/input-data-tf-data-%EC%9C%BC%EB%A1%9C-batch-%EB%A7%8C%EB%93%A4%EA%B8%B0-1c96f17c3696)
| [출처2](<https://locslab.github.io/Tensorflow-Dataset-API(2)/>)

기존에 pipeline 생성을 위해 사용하던 방법인 데이터를 tfrecord로 변환하고서 그 파일을 학습 데이터로 넣으려고 할 때 enqueue dequeue를 이용하면 코드도 복잡하고, 여러가지 불편함들을 많았다.

tf.data를 이용하면 편리하게 tfrecord를 열 수 있는 것 뿐만이 아니라 일반 이미지도 역시 손쉽게 배치로 생성하고 넣을 수 있다.

[tf.data로 input pipeline 만들기 예제](data_pipeline_ex.md)

<br>

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

<br>

## tf.data.Datasets 생성

먼저 디스크에 위치한 일반 데이터들을 tf.data.Datasets 객체로 만들기 위해서는 다음의 두가지 method가 이용된다.

- tf.data.Dataset.from_tensors()
- tf.data.Dataset.from_tensor_slice()

> 만약 저장된 데이터가 tfrecord format인 경우,
> tf.data.TFRecordDataset()를 이용하여 load 한다.
> TFRecordDataset 변환은 [여기]를 참조한다.

tf.data.Dataset.from_tensors()와 tf.data.Dataset.from_tensor_slice()의 차이점은
반환된 객체가 데이터 전체를 저장하느냐 여부이다.

<br>

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

<br>

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

<br>

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

<br>

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

<br>

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

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
