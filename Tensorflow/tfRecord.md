# TFRecord 변환 및 불러오기

`TFRecord`는 Tensorflow에서 지원하는 파일 형식으로,
dataset을 자체적인 바이너리 포맷으로 serialize해서 저장하는 파일 형식이다.
기본적으로는 Google의 Protocol Buffer와도 같다고 볼 수 있다.
[Google Protocol Buffer 참고](http://bcho.tistory.com/1182)

### Why TFRecord?

일반적으로 모델 학습시 image data와 레이블의 두가지 정보를 따로 불러
처리하게 되는데, 이렇게 두가지 정보를 따로 분리하여 관리하게 되면 이미지 정보와
이에 대응하는 레이블 정보를 matching해주는 코드가 추가되므로, 복잡해진다.

이에 반해, TFRecord 파일을 사용할 경우, 이미지 정보와 레이블 정보를
serialize하여 하나의 파일로 관리하기 때문에 별도의 작업없이 학습을 진행할 수 있다.

또한, 이미지 데이터가 jpg, png 등의 파일로 되어 있는 경우 매번 인코딩/디코딩 작업을
수행해 줘야 하기 때문에 학습시 비효율적인 측면이 있는데 반해, TFRecord는 파일 생성시
바이너리 데이터 포맷으로 변환해 저장하기에 이러한 부수적인 작업을 필요치 않는다.

마지막으로, 이미지 파일을 원본으로 관리하게 되면 파일 크기가 매우 커서 image dataset 자체가
차지하는 용량이 꽤 된다. TFRecord는 변환시에 이러한 파일 크기를 줄여주는 장점도 있다.

## TFRecord 변환 (저장하기)

image와 label을 serialize하여 저장

다음의 간략한 예제를 살펴보자

[[TFRecord 파일 생성 예제]]

[출처](https://digitalbourgeois.tistory.com/50)

```python
import tensorflow as tf


def bytes_feature(values):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))

def int64_feature(values):
  if not isinstance(values, (tuple, list)):
    values = [values]
  return tf.train.Feature(int64_list=tf.train.Int64List(value=values))

def read_imagebytes(imagefile):
    file = open(imagefile,'rb')
    bytes = file.read()
    return bytes

def main():
	image_data = read_imagebytes('/datset/images/000001.jpg')
	tf_example = tf.train.Example(features=tf.train.Features(feature={
		#feature 정보 입력
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(b'jpg'),
      'image/class/label': int64_feature(1),
      'image/height': int64_feature(75),
      'image/width': int64_feature(75),
	}))

	writer = tf.python_io.TFRecordWriter('/dataset/tfrecords/000001.tfrecord')
	writer.write(tf_example.SerializeToString())

if __name__ == "__main__":
    main()

```

예제에서는 height, width, 인코딩 포맷 (format), 이미지 바이너리 (encoded),
레이블 (class/label)등의 feature 정보를 생성한다.

생성된 feature 정보는 `tf.train.Features`객체를 이용하여,
`tf.train.Example` 인스턴스에 `feature` 파라미터로 전달하게 되는데 다음과 같이
dictionary 형태로 전달된다.

```python
feature={
		# feature 정보 입력
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(b'jpg'),
      'image/class/label': int64_feature(1),
      'image/height': int64_feature(75),
      'image/width': int64_feature(75),
	}
```

참고로 `image/encoded` key의 value인 데이터 이미지는 `bytes_feature`를 통해
tensorflow feature 타입으로 변환하여 전달된다. 이는 `tf.train.Feature(bytes_list=tf.train.BytesList(value=\[values\]))`와 동일하다.

이와같이 생성된 `tf.train.Example` 인스턴스를 `tf.python_io.TFRecordWriter`를 이용해서
tfrecord 파일에 써주는 것이다.

```python
writer = tf.python_io.TFRecordWriter('/dataset/tfrecords/000001.tfrecord')
writer.write(tf_example.SerializeToString())
```

## TFRecord 데이터 불러오기

저장된 TFRecord 데이터를 불러오는 방법은 tf.data.TFRecordDataset(filename) api 사용

TO-DOs:
다음 정리할 것

- [[조대협의 블로그: TFRecord]](https://bcho.tistory.com/1190)
- [[Daniil's blog: Tfrecords guide]](http://warmspringwinds.github.io/tensorflow/tf-slim/2016/12/21/tfrecords-guide/)
- [TF Dataset 모듈 및 TFRecord 사용법 정리 블로그](https://hcnoh.github.io/2018-11-05-tensorflow-data-module)
- [TFRecord 파일 생성 방법 (텐서플로우 데이타 포맷)](https://digitalbourgeois.tistory.com/50)
- [Using TFRecords and tf.Example](https://www.tensorflow.org/tutorials/load_data/tf_records)

##### [[Input Data Pipeline 만들기로 돌아가기]](data_pipeline.md)|[[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
