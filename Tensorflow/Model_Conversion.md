# Trained Model 변환하기

## Convert Keras Model (h5) to Tensorflow Model (ckpt)

```python
# Add ops to save and restore all the variables.
import keras
saver = tf.train.Saver()
model = keras.models.load_model("model.h5")
sess = keras.backend.get_session()
save_path = saver.save(sess, "/path/to_ckpt/model.ckpt")
```

> [출처: Stack overflow](https://github.com/keras-team/keras/issues/9040) <br><br>

## Convert Tensorflow model to Keras model

To be added <br><br>

## \* ML Model

ML Model은 대부분 Architecture와 Weights로 구성되며,
각 라이브러리마다 취급하는 방식이 약간씩 다르다. <br>
다음은 Tensorflow와 Keras에서 ML Model 취급 방식을 간략히 설명한다. <br>

### Keras Model [[출처]](https://jovianlin.io/saving-loading-keras-models/)

Keras는 ML 모델을 <br>
Option 1. Weights(.h5)와 Model Architecture (.json)으로 저장 및 불러오기 <br>
Option 2. Model 전체 (.h5)를 저장 및 불러오기 <br>
할 수 있다. <br>

- <b>[Option 1]</b> Weights and Model Architecture

> 저장하기 <br>

```python
# Save the weights
model.save_weights('model_weights.h5')
# Save the model architecture
with open('model_architecture.json', 'w') as f:
f.write(model.to_json())
```

> 불러오기

```python
from keras.models import model_from_json

# Model reconstruction from JSON file
with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())

# Load weights into the new model
model.load_weights('model_weights.h5')
```

<br>
- <b>[Option 2]</b> Entire Model <br>
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
4. State of the optimizer (allows you to resume the trainig from exactly where you left off)
   주: pickle 혹은 cPickle을 사용하여 keras model을 저장하는 방법은 권장하지 않는다. <br><br>

### Tensorflow Model

Tensorflow는 ML 모델을 저장/불러오기 하는 방식으로 checkpoint를 사용하거나 pd를 사용 할 수 있다.

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[Keras로 돌아기기]](https://github.com/elemag1414/Keras)[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
