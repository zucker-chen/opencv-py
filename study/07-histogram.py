import cv2.cv2 as cv
# import numpy as np
import matplotlib.pyplot as plt


def hist_display(src):
    plt.hist(src.ravel(), 256, [0, 256])
    plt.show()

def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"http://upload.taihainet.com/2016/0917/1474098004187.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
hist_display(src)
cv.waitKey(0)
cv.destroyAllWindows()
