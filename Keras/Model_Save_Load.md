# ML Model 저장/불러오기

ML Model은 대부분 Architecture와 Weights로 구성되며,
각 라이브러리마다 취급하는 방식이 약간씩 다르다. <br>
다음은 Keras에서 ML Model을 저장하고 불러오는 방법을 간략히 설명한다. [[출처]](https://jovianlin.io/saving-loading-keras-models/)

## Keras ML Model

Keras는 ML 모델을 <br>

- Option 1. Weights(.h5)와 Model Architecture (.json)으로 저장 및 불러오기 <br>
- Option 2. Model 전체 (.h5)를 저장 및 불러오기 <br>
  할 수 있다. <br>

### <b>[Option 1]</b> Weights and Model Architecture

#### 저장하기

```python
# Save the weights
model.save_weights('model_weights.h5')
# Save the model architecture
with open('model_architecture.json', 'w') as f:
f.write(model.to_json())
```

#### 불러오기

```python
from keras.models import model_from_json

# Model reconstruction from JSON file
with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())

# Load weights into the new model
model.load_weights('model_weights.h5')
```

<br>

### <b>[Option 2]</b> Entire Model

> 다음은 ML Model 전체를 하나의 h5파일로 저장하고 다시 불러오는 snippet이다.

```python
from keras.models import load_model

# Creates a HDF5 file 'my_model.h5'
model.save('my_model.h5')

# Deletes the existing model
del model

# Returns a compiled model identical to the previous one
model = load_model('my_model.h5')
```

하나의 hdf5 파일은 다음을 포함한다:

1. Architecture of the model (allowing the recreation of the model)
2. Weights of the model
3. Training configuration (e.g. loss, optimizer)
4. State of the optimizer (allows you to resume the trainig from exactly where you left off) <br>
   주: pickle 혹은 cPickle을 사용하여 keras model을 저장하는 방법은 권장하지 않는다. <br><br>

### Model Compile & Evaluation [[출처]](https://3months.tistory.com/150)

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