# Object Detection Model 학습을 위한 Annotation Tools

---

## labelImg

윈도우에서 많이들 사용하는것 같아서, MacOS를 사용하는 나로서는 별로 눈여겨 보지 않았지만,
아래 OpenCV CVAT나 RectLabel을 사용하다가 발생하는 번거로움 때문에 이 툴로 옮겨 왔다.

- GitHub: [[tzutalin/iabelImg]](https://github.com/tzutalin/labelImg)
- YouTube: [[데모]](https://youtu.be/p0nR2YsCY_U)

GitHub에 가보면 각 플랫폼 별로 설치 방법을 설명하고 있는데,
MacOS의 경우, Python이나 Qt 버전 문제로 설치에 어려움이 있는 모양이다.

설치 설명중 가상 환경에 설치하는 방법을 따라 설치 해봤다.

역시나, 설치가 제대로 되지 않는다. (우쒸...)

저자들은 Homebrew를 통해 python이나 기타 패키지를 설치/관리하는 모양인데,
나의 경우는 anaconda를 쓰기 때문에 중간 중간 경로 문제로 에러를 뱉어 낸다. ㅡㅡ;

약간의 삽질 끝에 해결한 방법을 다음과 같이 정리한다.
(anaconda 환경에서 python3.6으로 툴을 설치하는 방법)

```bash
#0. clone the git
   \$ git clone https://github.com/tzutalin/labelImg.git

#1. Make Virtual Env.
   \$ conda create --name LabelImg python=3.6

#2. install packages
   \$ pip install py2app
   \$ pip install PyQt5 lxml

#3. compile...
   \$ cd labelImg
   \$ make qt5py3
   \$ rm -rf build dist

#4. run setup
   \$ python setup.py py2app

#5. move app to Applications folder
   \$ mv "dist/labelImg.app" /ApplicationsPqflx

```

### Hotkeys

| Ctrl + u |  Load all of the images from a directory  |
| -------- | :---------------------------------------: |
| Ctrl + r | Change the default annotation target dir  |
| Ctrl + s |                   Save                    |
| Ctrl + d |    Copy the current label and rect box    |
| Space    |    Flag the current image as verified     |
| w        |             Create a rect box             |
| d        |                Next image                 |
| a        |              Previous image               |
| del      |       Delete the selected rect box        |
| Ctrl++   |                  Zoom in                  |
| Ctrl--   |                 Zoom out                  |
| ↑→↓←     | Keyboard arrows to move selected rect box |

---

## OpenCV CVAT

초기에 주로 썼던 툴이다.
무료이고 세그멘테이션 annotation과 대략적인 비디오 annotation등 여러 annotation 모드를 지원한다는 장점이 있다.
분명히 매우~ 강력한 툴이다. 하지만, bbox만을 주로 사용하기에는 이 툴이 약간 불편하다.
docker를 써야하고, bbox 생성시 박스 그리는 GUI가 좀 불편하다든지...

- GitHub: [[opencv/cvat]](https://github.com/opencv/cvat)
- 온라인 데모: [[데모]](https://c.onepanel.io/onepanel-demo/projects/cvat-public-demo/workspaces)

---

## RectLabel

MacOS 환경에서 세그멘테이션이나 bbox annotation 툴로써 이보다 깔끔한 디자인과 편리한 툴은 없어 보인다.
하지만, 한가지 아쉬움이자 함정은 유료라는 점.
처음 구글링해서 이 툴 찾았을때, 블로거가 마치 무료인냥 적어놔서
Appstore를 통해 설치 했더니,
2주간 사용해보고 유료로 구매하란다. (안한다. ㅡㅡ;;)

암턴 앱링크는 다음과 같다. 구경을 해보시던지... ㅎㅎ

- App [Link](https://rectlabel.com/)

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
