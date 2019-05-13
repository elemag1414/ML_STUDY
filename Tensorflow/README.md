# Tensorflow Tips

> Tensorflow는 Google에서 만든 ML 라이브러리로 현재 가장 널리 사용되는 플랫폼중 하나이다. <br>
> 다른 플랫폼에 비해 관리도 잘되고 documenation도 잘되어 있는 편이어서 개발자들이 선호하는듯 하다. <br>
> 하지만, 자주 갱신되는 api (2018년도부터 폭풍 update가 진행되고 있다.) 덕분에 따라잡기도 버겁다. <br>
> 개발에 필요한 내용과 나름 유용하다 생각되는 내용들을 정리해 본다. <br><br>

- Input Data Pipeline 만들기

  > > [For Image Classification](https://github.com/elemag1414/ML_STUDY/blob/master/Tensorflow/data_pipeline.md) <br>
  > > For Object Detection: To be added
  > > [Data Input Pipeline Performance](https://www.tensorflow.org/guide/performance/datasets)

- [Input Data를 TFRecode format으로 변환하기](tfRecord.md)

- Tensorflow ML Model API diagram : To be added

- Tensorflow APIs

  > > [Estimator API](https://www.tensorflow.org/api_docs/python/tf/estimator) <br> > > [Experiment API](https://www.tensorflow.org/api_docs/python/tf/experimental) <br> > > [Train API](https://www.tensorflow.org/api_docs/python/tf/train) <br>
  > >
  > > > see Train.Features also

- [Model 저장/불러오기](https://github.com/elemag1414/ML_STUDY/blob/master/Tensorflow/Model_Save_Load.md)

- [Trained Model 변환하기](https://github.com/elemag1414/ML_STUDY/blob/master/Tensorflow/Model_Conversion.md)

---

## ETC

- Install TF GPU

```bash
$ pip3 install --upgrade tensorflow-gpu
```

- [Tensorflow가 GPU를 사용하는지 확인하기](../Keras/keras_gpu.md)

- 특정 GPU만 사용하기

[[참고 블로그]](https://datamasters.co.kr/33)

tensorflow가 실행되면 default로 시스템의 모든 GPU 메모리를 차지하게 되는데,
이는 python 프로세스를 하나만 실행해도 GPU 메모리를 거의 다 차지하기에 자칫 OOM (out of memery)이 발생할 확률이 높아진다.

특히나, multi gpu 사용시 이러한 상황은 OTL이 아닐수 없다.

> shell에서 GPU에 python 실행 할당

```bash
$ CUDA_VISIBLE_DEVICES=0 python test1.py  # Uses GPU 0.

$ CUDA_VISIBLE_DEVICES=1 python test2.py  # Uses GPU 1.

$ CUDA_VISIBLE_DEVICES=2,3 python test3.py  # Uses GPUs 2 and 3.
```

> python 스크립트에서 GPU 할당

```python
import os

os.environ["CUDA_DEVICE_ORDER"]='PCI_BUS_ID'
os.environ["CUDA_VISIBLE_DEVICES"]='0'        # Uses GPU 0
# os.environ["CUDA_VISIBLE_DEVICES"]='0,1'      # Uses GPU 0 & GPU 1

```

> with tf.device를 사용하는 방법

with 문을 사용하여 tf가 사용하는 device를 설정하는 방법

```python

import tensorflow as tf

# CPU만 사용하기
with tf.device('/cpu:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2,3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3,2], name='b')

# GPU만 사용하기
with tf.device('/device:GPU:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2,3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3,2], name='b')
  c = tf.matmul(a, b)

# Create a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# Run the op.
print(sess.run(c))

```

이 방식의 단점은 with문을 지속적으로 지정해줘야 해서 매우 불편함.

> tf.ConfigProto().gpu_options을 사용한 지정

tf에서는 gpu 메모리 지정 방식을 바꿀 수 있는 두가지 옵션을 제공한다.

> > `allow_growth`

다음과 같이 설저하면 GPU 메모리가 전부 할당되지 않고, 연산 시작시 적은 비율만 할당되다가 프로세스의 메모리 수요에 따라 할당량이 증가하게 된다.

```python

import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

```

이 방법을 사용하게 되면 적어도 GPU의 모든 메모리를 잡아먹는 상황을 피할 수 있게 된다.

**주의할 점은, 이 옵션은 메모리 증식만 가능하다는 것**이다. 연산이 끝나고 메모리가 필요없는 상황이 되도 할당된 메모리를 반납하지 않게 되므로, tf는 이 경우 더 심한 메모리 파편화가 발생할 수 있다.

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
