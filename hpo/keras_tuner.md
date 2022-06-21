# Hyper Parameter Optimiztion with Keras Tuner

##### [Back to ML-Study Home](../README.md)

* References:
  - [Hyperparameter Tuning in Python: a Complete Guide](https://neptune.ai/blog/hyperparameter-tuning-in-python-complete-guide)
  - [Keras Tuner: Lessons Learned From Tuning Hyperparameters of a Real-Life Deep Learning Model](https://neptune.ai/blog/keras-tuner-tuning-hyperparameters-deep-learning-model)
  - [Keras Tuner (keras official)](https://keras.io/keras_tuner/)


### Quick Introduction

1. Install ```keras-tuner``` library

```
$ pip3 install keras-tuner # --upgrade to upgrade installed module
```


2. Basic Structure

HPO with ```keras-tuner``` consists of three parts:
- ```build_model(hp)```: creates and returns a Keras model. arg ```hp``` is used to define hyper parameters to tune-up.
- ```keras_tuner.<tune_method>```: initialize and setup search method. ```<tune_method>```: ```RandomSearch```, ```Hyperband```, ```BayesianOptimization```, and more.
- ```tuner.search```: start the search and find the best model

Let's take a look with some example snippets:

* Import Modules

```python
import keras_tuner
from tensorflow import keras
```

* ```build_model()```
 
```python
def build_model(hp):
  model = keras.Sequential()
  model.add(keras.layers.Dense(
      hp.Choice('units', [8, 16, 32]),
      activation='relu'))
  model.add(keras.layers.Dense(1, activation='relu'))
  model.compile(loss='mse')
  return model
```

* define ```tuner```
```python
tuner = keras_tuner.RandomSearch(
    build_model,
    objective='val_loss',
    max_trials=5)
```


* search the optimal
```python
tuner.search(x_train, y_train, epochs=5, validation_data=(x_val, y_val))
best_model = tuner.get_best_models()[0]
```

##### [Back to ML-Study Home](../README.md)
