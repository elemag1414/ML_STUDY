# Keras 모델(h5) 텐서보드로 보기

> TODO: 학습된 Keras 모델을 직접 텐서보드로 확인하는 방법

학습된 Keras 모델을 텐서보드로 확인기 위해선 현재로서는 번거롭지만,
h5 파일을 pb파일로 변환한 후 이를 텐서보드 log를 생성하는 방식으로 보여주는 방식을 사용한다.

1. Keras 모델(h5)을 pb로 변환
   [Trained Model 변환하기](https://github.com/elemag1414/ML_STUDY/blob/master/Tensorflow/Model_Conversion.md)에서 h5를 pb로 변환하는 방법을 참조

2. pb 파일 텐서 보드 로그 생성하기
   pb 파일 텐서 보드 로그 생성하는 방법은 tensorflow/python/tools/import_pb_to_tensorboard.py의 `import_to_tensorboard` method를 사용한다.

3. 텐서보드로 확인하기
   상기 절차를 통해 log가 생성되면,
   `tensorboard --logdir=./log'로 텐서보드를 실행하여 브라우저로 확인한다.

> > 예제 ([Generate_Graph_from_h5](Generate_Graph_from_h5.py)보기)

```bash
python Generate_Graph_from_h5 --model_dir modelpath/h5model.h5 --log_dir ./log
```

`--model_dir` h5 파일 위치 option
`--log_dir` 텐서보드 로그가 생성될 path

##### [[Keras로 돌아기기]](README.md)|[[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
