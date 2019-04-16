# Datasets 변환(transformation)하기

`tf.data.Datasets` 객체가 생성되면 method들을 호출하여 `tf.data.Datasets`을 여러가지형태로 transformation 할 수 있다.

예를들어 각 요소(element) 별로도 변형이 가능 (ex. `tf.data.Dataset.map()`) 하고,

전체 데이터셋에 대해서도 변형이 가능하다. (ex. `tf.data.Dataset.batch()`).

`tf.data.Datasets`은 transformation과 관련된 다음과 같이 많은 method들이 있는데 해당하는 method들의 list는
해당 링크를 통해 확인한다. [[tf.data.Dataset API]](https://www.tensorflow.org/api_docs/python/tf/data/Dataset):

- [.apply(): transformation 적용](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)
- [.concatenate()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#concatenate)
- [.filter()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#filter)
- [.flat_map()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#flat_map)
- [.interleave()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
- [.map()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)
- [.reduce()](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#reduce)

##### [[Input Data Pipeline 만들기로 돌아가기]](data_pipeline.md#transformation과-iterator)|[[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
