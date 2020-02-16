import cv2.cv2 as cv
import numpy as np


def harris_corner_detect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (9, 9), 25)  # sigma
    # cv.imshow('GS gray', gray)
    # dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.cornerHarris(gray, 9, 19, 0.06)
    # 膨胀腐蚀-开操作，去除小的干扰角点
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
    dst = cv.morphologyEx(dst, cv.MORPH_OPEN, kernel)
    # 角点绘制
    # image[dst > 0.01 * dst.max()] = [0, 0, 255]
    image[dst > 0.01 * dst.max()] = [0, 0, 255]
    cv.imshow('image for harris', image)


def fast_corner_detect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (9, 9), 25)  # sigma
    fast = cv.FastFeatureDetector_create()
    kp = fast.detect(gray, None)
    image = cv.drawKeypoints(image, kp, None, color=(255, 0, 0))
    cv.imshow('image for fast', image)


def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"http://pic.616pic.com/bg_w1180/00/22/32/dekWPCrqb9.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
harris_corner_detect(src.copy())
fast_corner_detect(src.copy())
cv.waitKey(0)
cv.destroyAllWindows()
