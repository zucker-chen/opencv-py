import cv2.cv2 as cv
import numpy as np

def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


# 均值模糊（均值滤波）
def img_blur(img):
    dst = cv.blur(img, (5, 5))
    cv.imshow("blur", dst)


# 中值模糊（中值降噪）
def img_medianblur(img):
    dst = cv.medianBlur(img, 5)
    cv.imshow("median blur", dst)


# 自定义模糊处理
def img_custom_blur(img):
    kernel = np.ones([5, 5], np.float) / (5 * 5)    # 均值模糊
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float)  # 锐化
    dst = cv.filter2D(img, -1, kernel = kernel)
    cv.imshow("custom blur", dst)


def img_gaussian_blur(img):
    # dst = cv.GaussianBlur(img, (0, 0), 15)  # sigma
    dst = cv.GaussianBlur(img, (5, 5), 0)  # x
    cv.imshow("gasuss blur", dst)



src = net_imread(r"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3593466601,372981957&fm=26&gp=0.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
img_blur(src)
img_medianblur(src)
img_custom_blur(src)
img_gaussian_blur(src)
cv.waitKey(0)
cv.destroyAllWindows()

