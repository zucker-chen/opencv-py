import cv2.cv2 as cv
import numpy as np


# 全局阈值
def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    print("阈值：", ret)
    cv.imshow("binary", binary)


# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGRA2GRAY)
    # binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,25,10)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("adaptive ", binary)


# 自定义二值化
def custom_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGRA2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("custom ", binary)


def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"https://tuzhizhijia.com/uploads/allimg/180808/1535121527-0.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
threshold_demo(src)
local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
