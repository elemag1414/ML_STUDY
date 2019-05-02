# Object Detection Model 학습을 위한 Annotation Tools

##. labelImg

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

##. OpenCV CVAT
초기에 주로 썼던 툴이다.

- GitHub: [[tzutalin/iabelImg]](https://github.com/tzutalin/labelImg)
- YouTube: [[데모]](https://youtu.be/p0nR2YsCY_U)

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)

```

```

```

```
