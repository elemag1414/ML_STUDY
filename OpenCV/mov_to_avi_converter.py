import cv2
import argparse
from os.path import isfile
import sys
from tqdm import tqdm


# Video Config
WINDOW_NAME = "Video"
OUTPUT_WIDTH = 1902  # 640
OUTPUT_HEIGHT = 1080  # 480
recordFlag = False
showFlag = True


# Arg Parse
parser = argparse.ArgumentParser(description='Mov to Avi Converter')
parser.add_argument('--input', required=True,
                    help='path to input image file')
parser.add_argument('--output', help='path to output image')
args = parser.parse_args()

im_file = args.input
rec_file = args.output

if rec_file is None:
    print('input: {} and No Output is specified'.format(args.input))
else:
    print('Convert {} to {}'.format(args.input, args.output))
    recordFlag = True
    # Check if output video file name already exists
    if isfile(rec_file) == True:
        print('Output file {} already exists'.format(rec_file))
        sys.exit()

# Check if input video exists
if isfile(im_file) == False:
    print('Input file not found')
    sys.exit()


def OpenRecDevice(outputfile, Width, Height):
    fps = 20  # Frame Per Second
    # For MacOS use MJPG and avi as extension, for Window use DIVX and avi as extension
    # fourcc = cv2.VideoWriter_fourcc(*"MJPG") # For MacOS
    fourcc = cv2.VideoWriter_fourcc(*"DIVX")  # For MacOS
    rec = cv2.VideoWriter(
        outputfile, fourcc,
        fps, (Width, Height)
    )
    return rec


def main():
    # Open Webcam resources
    cap = cv2.VideoCapture(im_file)

    if (cap.isOpened() == False):
        print("Error opening video clip")

    nFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # print('total # frames: {}'.format(nFrames))

    if recordFlag:
        _, _image = cap.read()
        width = _image.shape[1]
        height = _image.shape[0]
        rec = OpenRecDevice(rec_file, width, height)

    # Create Window
    if showFlag:
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(WINDOW_NAME, OUTPUT_WIDTH, OUTPUT_HEIGHT)

    i = 1
    pbar = tqdm(total=nFrames, initial=i)

    # while True:
    while i <= nFrames:

        _, image = cap.read()

        if showFlag:
            cv2.imshow(WINDOW_NAME, image)

        # Save the results
        if recordFlag:
            rec.write(image)

        i += 1
        pbar.update(1)

        if showFlag:
            # Keyboard interrupt
            keyPressed = cv2.waitKey(5)

            if keyPressed == 27 or keyPressed == 1048603:  # esc to escape
                print("Quit")
                break
            elif keyPressed == 80 or keyPressed == 112:  # p to pause
                print("Pause...")
                while True:
                    cv2.imshow(WINDOW_NAME, image)
                    keyPressed = cv2.waitKey(5)
                    if keyPressed == 80 or keyPressed == 112:  # p to continue
                        print("Continue...")
                        break

    pbar.close()

    # release camera resources
    cap.release()

    # release recording resources
    if recordFlag:
        rec.release()

    # Close all pop-up windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


import cv2

recordFlag = False


def OpenRecDevice(outputfile, Width, Height):
    fps = 20  # Frame Per Second
    # For MacOS use MJPG and avi as extension, for Window use DIVX and avi as extension
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    rec = cv2.VideoWriter(
        outputfile, fourcc,
        fps, (Width, Height)
    )
    return rec


# Open Webcam resources
im_file = ''
rec_file = ''
cap = cv2.VideoCapture(im_file)

if (cap.isOpened() == False):
    print("Error opening video clip")


if recordFlag:
    _, _image = cap.read()
    width = _image.shape[1]
    height = _image.shape[0]
    rec = OpenRecDevice(rec_file, width, height)


while True:

    _, image = cap.read()

    # image = cv2.UMat(_image) # for GPU Process

    # Visualize Video
    WINDOW_NAME = "Video"
    OUTPUT_WIDTH = 640
    OUTPUT_HEIGHT = 480
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, OUTPUT_WIDTH, OUTPUT_HEIGHT)
    cv2.imshow(WINDOW_NAME, image)

    # Save the results
    if recordFlag:
        rec.write(image)

    # Keyboard interrupt
    keyPressed = cv2.waitKey(5)

    if keyPressed == 27 or keyPressed == 1048603:  # esc to escape
        print("Quit")
        break
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
