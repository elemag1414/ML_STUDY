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

##### [[Tensorflow로 돌아가기]](https://github.com/elemag1414/ML_STUDY/tree/master/Tensorflow)|[[Keras로 돌아기기]](https://github.com/elemag1414/Keras)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
