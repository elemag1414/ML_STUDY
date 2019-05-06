# 2019-05-06

## Drone

- 20190410 Drone Data Train Model로 Drone Video 시험
  > 결과가 만족할 만한 수준은 아님. 작은 크기는 여전히 검출을 못함
  > 0408 데이터를 추가하여 학습 하기로 함
- 20190408 Drone Data Annotation 작업하여 20190410 Data Annotation과 병합
- aerial_pedestrian_detection를 이용하여 20190408_10 Drone Data Training

## LPWA

- 발표자료 검토 및 수정

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
