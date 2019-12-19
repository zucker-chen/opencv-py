import cv2.cv2 as cv
import numpy as np


def img_ch_split(img):
    r, g, b = cv.split(img)
    # cv.imshow("r", r)
    # cv.imshow("g", g)
    # cv.imshow("b", b)
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    cv.imshow("ch0", img)
    bgr = cv.merge([b, g, r])
    cv.imshow("bgr", bgr)

def img_color_filter(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # color orange
    low_hsv = np.array([11, 43, 46])
    up_hsv = np.array([25, 255, 255])
    mask = cv.inRange(hsv, lowerb=low_hsv, upperb=up_hsv)
    cv.imshow("filter", mask)


def video_color_demo():
    cap = cv.VideoCapture("http://vfx.mtime.cn/Video/2019/03/19/mp4/190319222227698228.mp4")
    while (True):
        ret, frame = cap.read()
        if ret == False:
            break
        # img_color_filter(frame)
        img_ch_split(frame)
        # cv.imshow("video", frame)
        c = cv.waitKey(40)
        if c == 27:
            break




#cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
video_color_demo()
#cv.waitKey(0)
cv.destroyAllWindows()


