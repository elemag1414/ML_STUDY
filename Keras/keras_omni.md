# Keras 관련 이모 저모

ㅇ

---

## Callback?

[[출처]](https://keras.io/callbacks/)

A **callback** is a set of functions to be applied at given stages of the training procedure. You can use callbacks to get a view on internal states and statistics of the model during **training**. You can pass a list of callbacks (as the keyword argument callbacks) to the .fit() method of the Sequential or Model classes. The relevant methods of the callbacks will then be called at each stage of the training.

Keras 모델 (`model`) **training**시 `model.fit_generator()`의 인자로 자주 이용되며,
사용자가 정의한 함수들을 `list`로 만들어 (e.g., `custom_list = [def_a, def_b]`)

```python
model.fit_generator(..., callbacks=custom_list)
```

와 같은 형태로 많이 사용된다.

---

##### [[Keras로 돌아기기]](README.md)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
