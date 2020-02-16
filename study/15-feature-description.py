import cv2.cv2 as cv
import numpy as np


def sift_feature_descript(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sift = cv.xfeatures2d.SIFT_create()
    # 图像中查找关键点, 如果只想搜索图像的一部分，可以传递掩膜
    kp = sift.detect(gray, None)
    # DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,它将绘制一个大小为keypoint的圆圈并显示它的方向
    cv.drawKeypoints(gray, kp, image, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow('sift point', image)




def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"http://image001.yambs.net/20170720/b2a9043ac1c6b1ecb142f3f84963f822.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
sift_feature_descript(src)
cv.waitKey(0)
cv.destroyAllWindows()
