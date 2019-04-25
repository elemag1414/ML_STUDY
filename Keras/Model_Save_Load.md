# ML Model 저장/불러오기

ML Model은 대부분 Architecture와 Weights로 구성되며,
각 라이브러리마다 취급하는 방식이 약간씩 다르다. <br>
다음은 Keras에서 ML Model을 저장하고 불러오는 방법을 간략히 설명한다. [[출처]](https://jovianlin.io/saving-loading-keras-models/)

---

## Keras ML Model

Keras는 ML 모델을 저장과 불러오는 방법으로 다음 2가지의 방식이 있다.<br>

- Option 1. Model 전체 (.h5)를 저장 및 불러오기 <br>
- Option 2. Model의 Weights(.h5)와 Model Architecture (.json)를 따로 저장 및 불러오기 <br>
  할 수 있다. <br>

---

### 저장하기

0. 가정
   ML 모델 `model` object는 `keras.Sequential`로 이미 생성되어 가정한다.

#### Keras 모델 전체 저장하기

```python
model.save('model_keras.h5')
```

`model.save()` method는 keras로 생성된 모델 전체를 저장하며,
구체적으로 다음을 저장한다.

- The architecture of the model allowing to re-create the model
- The weights of the model
- The training configuration (loss, optimizer)
- The state of the optimizer allowing to resume training exactly where you left off.

  주: pickle 혹은 cPickle을 사용하여 keras model을 저장하는 방법은 권장하지 않는다.

#### Weights와 Architecture 따로 저장하기

```python
# Save the weights
model.save_weights('model_weights.h5')
# Save the model architecture
with open('model_architecture.json', 'w') as f:
f.write(model.to_json())
```

---

### 불러오기

#### Keras 모델 전체 불러 오기

```python
from keras.models import load_model
model = load_model('model_keras.h5')
```

> 불러온 모델은 `.summary()` method로 구성을 확인할 수 있다

```python
model.summary()
```

> 마찬가지로 불러온 모델로 부터 weights와 optimizer정보도 따로 확인할 수 있다

```python
model.get_weights()
model.optimizer
```

<br>

#### Weights와 Architecture 따로 불러오기

> Architecture만 불러오기
>
> > Architecture만 불러오는 경우, 모델의 구조만 불러오고 training configuration과 Weights 정보는 가져 오지 않는다.

```python
from keras.models import model_from_json

# Model Architecutre only from JSON file
with open('model_architecture.json', 'r') as f:
    model_architecture = model_from_json(f.read())
```

> > 불러온 architecture는 `.summary()`를 통해 확인할 수 있다.

<br>

> Weights만 불러오기
>
> > 이 경우는 Weights를 불러오기 위한 모델 구조를 먼저 생성해주고, Weights를 불러오는 단계를 거친다. 이때 생성하는 모델 구조는 불러올 Weights를 만들었던 ML 모델 구조와 동일 해야 한다.

```python
# Load weights into the new model
# To load weight from the file,
# You need to constructe the same architure as saved first
# And then you can load weights.
# For instance,
# constructe Architecture
model = Sequential([
    Dense(16, input_shape(1,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')
])
# Then, load weights
model.load_weights('model_weights.h5')
```

### Model Compile & Evaluation [[출처]](https://3months.tistory.com/150)

---

Model 불러오기를 통해 Keras Model이 준비 되었다면, compile 후 evaluation 과정을 추가 할 수 있다.

예제를 위해 입력 데이터 세트 X와 ground truth Y가 있다고 가정하면 다음을 통해 성능 평가를 할 수 있다.

> Model Compile

```python
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=['accuracy'])
```

> Model Evaluation

```python
score = model.evaluate(X,Y,verbose=0)
```

> Print Results

```python
print("{} : {:%.2f}".format(model.metrics_names[1], score[1]*100))
```

#### Additional Resources:

- [h5py: Python에서 HDF5 파일 읽고 쓰기](https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html)

##### [[Keras로 돌아기기]](https://github.com/elemag1414/Keras)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
