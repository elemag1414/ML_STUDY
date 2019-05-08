# 2019-05-09

## Drone

- [ ] diff filter: ObjectDetection/ObjectTracking/re3/demo/detection_test.py

## LPWA

- [ ] 발표자료 수정

## etc

---

# 2019-05-08

## Drone

- [x] aerial_pedestrian_detection를 이용하여 201904_02_05_08_10 Drone Data Training 계속

- [ ] Yolo v3과 성능 비교를 위한 모델 준비

  > 코드 clone 및 수정
  > Yolo v3 학습을 위한 데이터세트 준비 작업

- [ ] Small Object 검출을 위한 Background Study

  > "Unsupervised learning from Video to detect foreground objects in single images"
  >
  > > Paper: [ICCV 2017 paper](http://openaccess.thecvf.com/content_ICCV_2017/papers/Croitoru_Unsupervised_Learning_From_ICCV_2017_paper.pdf)
  > > Code: [GitHub](https://github.com/ioanacroi/unsup-learning-from-video/)

  > "Unsupervised object segmentation in video by efficient selection of highly probable positive features"
  >
  > > Paper: [ICCV 2017 paper](https://arxiv.org/pdf/1704.05674.pdf)
  > > Code: [MATLAB Version](https://drive.google.com/drive/folders/0BxYHPeDp3MzoRHpyOGhFRGxyLWM)
  > > Web: [Paper Web](https://sites.google.com/view/unsupervisedobjectsegmentation/home)

## LPWA

- [x] 발표자료 검토 회의

## etc

---

# 2019-05-07

## Drone

- [x] 20190402, 20190405 DataSet Annotation 작업하여 기존 201904_08_10 DataSet에 병합 (201904_02_05_08_10 Dataset 생성)
- [x] aerial_pedestrian_detection를 이용하여 201904_02_05_08_10 Drone Data Training
  > Batch Step Size를 1000으로 한 경우, mAP가 201904_08_10 DataSet으로 Training시와 비교하여 낮게 학습되어, 2000으로 변경하여 학습 진행
  > ToDo: 학습시 GPU 모니터해보니 생각보다 많은 시간이 idle로 보임. 학습 시간 단축을 위한 분석 필요

## etc

---

# 2019-05-06

## Drone

- [x] 20190410 Drone Data Train Model로 Drone Video 시험
  > 결과가 만족할 만한 수준은 아님. 작은 크기는 여전히 검출을 못함
  > 20190408 데이터를 추가하여 학습 하기로 함
- [x] 20190408 Drone Data Annotation 작업하여 20190410 Data Annotation과 병합
- [x] aerial_pedestrian_detection를 이용하여 20190408_10 Drone Data Training

## LPWA

- [x] 발표자료 검토 및 수정

## etc

---

# 2019-05-05

## Drone

- 20190410 Drone Data Annotation 작업
- aerial_pedestrian_detection를 이용하여 20190410 Drone Data Training

## etc

---

# 2019-05-03

## Drone

- 프로토콜 검토 회의

## LPWA

- 발표자료 검토 회의

## etc

-

---

# 2019-05-02

## Drone

- Aerail Images에서 RetinaNet을 이용한 소형 물체 검출 (aerial_pedestrian_detection) 모델 코드 분석

  > [코드](https://github.com/priya-dwivedi/aerial_pedestrian_detection) 분석

- 주/야간 영상 센서 시험/데모

## etc

- [x] aerial_pedestrian_detection 모델 1차 학습 결과 분석
  > > Epoch 50을 마친후, Eval 툴을 사용하여 성능 분석해보니, 성능이 알려진 내용보다 안 좋음. 또한, Eval시 오류 메시지 출력 (To-Do Issue: Debug 할것)
- [x] `labelImg` Annotation Tool 설치 (MacOS에 설치시 오류 발생했으나 해결)
- [ ] Layer Output Visualization (ToDo: Check out the layer output of consecutive frames)

---

# 2019-05-01

## Drone

- RetinaNet Keras 코드 분석

  > [코드](https://github.com/fizyr/keras-retinanet) 분석

- 과제 GPU Server에서 Aerail Images에서 RetinaNet을 이용한 소형 물체 검출 모델 학습
  > 5/10 오후 6:15에 Epoch 46/50 학습 진행 확인 (loss:0.126, r_loss:0.12, c_loss:0.0071)

## etc

- [x] 시험용 Drone dataset annotion 작업 (약 20장) / RectLabel 툴을 사용 (14일 한정판)
- [x] 생성 annotation을 dataset에서 눈으로 검증하는 루틴 작성
- [x] RectLabel에서 생성한 xml 라벨 파일을 parsing하여 xml keras-retinanet 모델 학습에 사용할 수 있도록 csv 생성 코드 작성
- [x] HD 사이즈 이상 큰 이미지 HD로 변경 루틴 작성
- [ ] Layer Output Visualization (ToDo: Check out the layer output of consecutive frames)

---

# 2019-04-30

## Drone

- RetinaNet Keras 코드 분석

  > [코드](https://github.com/fizyr/keras-retinanet) 분석

- [x] 과제 GPU Server에서 Aerail Images에서 RetinaNet을 이용한 소형 물체 검출 모델 학습 (30일 오후 2시쯤 시작)
- [x] 과제 특허 권리 분석 kick-off 참석

## LPWA

- 발표자료: 기술의 우수성 부분 작성중

## etc

- [ ] Hog Feature Study
- [ ] Layer Output Visualization (ToDo: Check out the layer output of consecutive frames)

---

# 2019-04-29

## Drone

- RetinaNet Keras 코드 분석

  > [코드](https://github.com/fizyr/keras-retinanet) 분석
  > 모델 생성시 Backbone과 interference 부분 생성 시점 확인
  >
  > > 모델 불러오기 시점에 RetinaNet weight가 모델의 어느부분까지 load되는지 확인

- [x] 과제 GPU Server 검수

## LPWA

- 발표자료: 기술의 우수성 부분 작성중

## etc

- [x] h5 file Tensor board로 확인하기
- [ ] Hog Feature Study
- [ ] Layer Output Visualization (ToDo: Check out the layer output of consecutive frames)

---

# 2019-04-26

## Drone

- RetinaNet Keras 코드 분석

  > [코드](https://github.com/fizyr/keras-retinanet) 분석
  > 모델 생성시 Backbone과 interference 부분 생성 시점 확인
  >
  > > 모델 불러오기 시점에 RetinaNet weight가 모델의 어느부분까지 load되는지 확인

- [x] 과제 업무회의

## LPWA

- 발표자료: 기술의 우수성 부분 작성중

## etc

- [ ] h5 file Tensor board로 확인하기
- [ ]

---

# 2019-04-25

## Drone

- RetinaNet Keras 코드 분석
  > [코드](https://github.com/fizyr/keras-retinanet) 분석
  > [x] Training 방법 검토
  > [x] Anchor Box 변경 ([블로그](https://towardsdatascience.com/pedestrian-detection-in-aerial-images-using-retinanet-9053e8a72c6) 참조)
- Focal Loss 분석

## LPWA

- [x] 발표자료 검토

## etc

- [x] tf.keras API Tensor 보드 사용하기 Study
- [ ]

---

# 2019-04-24

## Drone

- Re3 Training 분석
- Focal Loss 분석

## LPWA

- 발표자료 검토

## Smart City

- 규격 수정

## etc

- [x] vscode docker 연동 예제
      [Dan Taylor - From Zero to Azure with Python, Docker containers, and Visual Studio Code](https://www.youtube.com/watch?v=I1cG1FRjFOQ)

- [x] vscode docker compose 예제
      [Easy Docker Dev to Production Setup for Small Projects](https://www.youtube.com/watch?v=LSyIE-bTt5U)
