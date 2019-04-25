# tf.keras에서 Tensorboard 사용하기

### 모듈 import

```python
# tf.keras frequently used modules
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

# Keras Tensorboard callback
from tensorflow.keras.callbacks import TensorBoard

# ETC
import time
```

### 생성될 모델 이름 정하기

```python
NAME = "MyModel-cnn-64x2-{}".format(int(time.time()))
```

`NAME`은 추후 Tensorboard 로그가 생성될 directory 이름으로 사용될 것 이며, 이때 동일한 이름 지정으로 발생하는 번거로움을 해소하고자, 생성다시의 timestamp를 모델 이름으로 정한다.

동일한 모델명으로 정하면, 추후의 training시 학습된 모델이 기존에 동일한 이름으로 저장된 모델 파일에 append형태로 추가되므로, tensorboard 확인시 기존 log정보에 덧대 표시되면서 나타나는 zig-zag 모양이 될 수 있어 결과 분석을 방해하는 일이 발생할 수 있다.

### 생성된 log 정보 저장 directory 지정

```python
tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))
```

log 정보는 `log_dir`에 의해 지정된 directory로 저장된다.

### tensorboard log 정보 생성을 위한 callback 지정

```python
model = Sequential()
...

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3, callbacks=[tensorboard])
```

여기서, callback이 `.fit()' method에 추가 되었다. training 동안 log 정보를 생성해 줄 것이다. 주: 여기서`callbacks` 인자의 값은 list로 전해야 한다.

### 생성된 tensorboard log 정보 보기

오류없이 정상적인 학습이 진행되면, tensorboard를 통해 학습 진행과정을 살펴볼 수 있다.

이를 확인하기 위해, 우선 터미널을 열어 프로젝트 directory(`log_dir`가 아님)로 이동 후,

```bash
$prj_dir> tensorboard --logdir=logs
TensorBoard 1.10.0 at localhost:6006 (Press CTRL+C to quit)
```

상기 command를 수행하면 화면에 사용 port가 표시될 것 이다. Web browser에 해당 port를 사용하여 page를 열면 tensorboard가 나타날 것이다.

##### [[Keras로 돌아기기]](README.md) | [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
