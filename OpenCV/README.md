# OpenCV

## Codes or Snippets

- [Mov to AVI Converter](mov_to_avi_converter.md)

---

## Summary

### Contents

- [OpenCV 도형 그리기](#OpenCV-도형-그리기)
- [Color Constants](#Color-Constants)
- [Image Read](#Image-Read)
- [Video Control](#Video-Control)
- [Webcam Control](#Webcam-Control)

---

- [OpenCV 도형 그리기](https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html)

  > > 도형 그릴때 thickness를-1로 주면 내부가 채워진 도형이 된다.

- Color Constants

```python
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
white = (255,255,255)
yellow = (0,255,255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)
```

- Image Read

```python
import cv2

filename = Sample.JPG
image = cv2.imread(filename)
Width = image.shape[1]
Height = image.shape[0]

WINDOW_NAME = "Image"
# OUTPUT_WIDTH = 640
# OUTPUT_HEIGHT = 480
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL) # Make Window Resizable
# cv2.resizeWindow(WINDOW_NAME, OUTPUT_WIDTH, OUTPUT_HEIGHT)
cv2.imshow(WINDOW_NAME, image)

# Key Interrupt
keyPressed = cv2.waitKey()

if keyPressed == 27 or keyPressed == 1048603:  # esc to escape
    print("Quit")
    break

#cv2.imwrite(inputArgs.output, image)
cv2.destroyAllWindows()
```

<br>

- Video Control

```python
import cv2

video_resolution = {'SD': (720, 480), 'HD': (
    1280, 720), 'FHD': (1920, 1080), '4k': (4096, 2160)}

recordFlag = False

def OpenRecDevice(outputfile, Width, Height,fps):
    # For MacOS use MJPG and avi as extension, for Window use DIVX and avi as extension
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    rec = cv2.VideoWriter(
        outputfile, fourcc,
        fps, (Width, Height)
    )
    return rec


# Open Webcam resources
im_file = sample_input.mov
rec_file = sample_ouput.MP4
cap = cv2.VideoCapture(im_file)
fps = cap.get(cv2.CAP_PROP_FPS)
numFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fwidth = int(cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH))
fheight = int(cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT))

if (cap.isOpened() == False):
    print("Error opening video clip")


if recordFlag:
    _, _image = cap.read()
    width = _image.shape[1]
    height = _image.shape[0]
    rec = OpenRecDevice(rec_file, width, height, fps)

frm_cnt = 0
rewind_key = False
forward_key = False
while True:

    if rewind_key:
        if frm_cnt > fps * 3:
            cap.set(1, int(frm_cnt - fps * 3))
            frm_cnt -= int(fps * 3)
        else:
            cap.set(1, 0)
            frm_cnt = 0
        rewind_key = False
    elif forward_key:
        cap.set(1, int(frm_cnt + fps * 3))
        frm_cnt += int(fps * 3)
        forward_key = False
    else:
        frm_cnt += 1
    _, image = cap.read()

    # image = cv2.UMat(_image) # for GPU Process

    # Visualize Video
    WINDOW_NAME = "Video"
    # OUTPUT_WIDTH = 640
    # OUTPUT_HEIGHT = 480
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(WINDOW_NAME, OUTPUT_WIDTH, OUTPUT_HEIGHT)
    if image is None:
        print("No Image to show... Exit")
        break
    cv2.imshow(WINDOW_NAME, image)

    # Save the results
    if recordFlag:
        rec.write(image)

    # Keyboard interrupt
    keyPressed = cv2.waitKey(5)

    if keyPressed == 27 or keyPressed == 1048603:  # esc to escape
        print("Quit")
        break
    elif keyPressed == 74 or keyPressed == 106:  # j to move back 1sec
        print("Rewind to 1 sec")
        rewind_key = True
    elif keyPressed == 75 or keyPressed == 107:  # k to move forward 1sec
        print("Forward to 1 sec")
        forward_key = True
    elif keyPressed == 80 or keyPressed == 112:  # p to pause
        print("Pause...")
        while True:
            cv2.imshow(WINDOW_NAME, image)
            keyPressed = cv2.waitKey(5)
            if keyPressed == 80 or keyPressed == 112:  # p to continue
                print("Continue...")
                break

# release camera resources
cap.release()

# release recording resources
if recordFlag:
    rec.release()

# Close all pop-up windows
cv2.destroyAllWindows()

```

<br>

- Webcam Control

```python
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    # Keyboard interrupt
    keyPressed = cv2.waitKey(3)

    if keyPressed == 27 or keyPressed == 1048603:  # esc to escape
        print("Quit")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

##### [[ML_STUDY로 돌아기기]](https://github.com/elemag1414/ML_STUDY)
