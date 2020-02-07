import cv2.cv2 as cv
import numpy as np


# 测量边缘
def edge_measure(image, contours):
    for i, contour in enumerate(contours):  # 遍历全部轮廓
        area = cv.contourArea(contour)
        # cv.boundingRect返回四个参数（x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高
        x, y, w, h = cv.boundingRect(contour)  # 外接矩形大小
        rate = min(w, h) / max(w, h)            # 宽高比
        # 计算图像中的中心矩
        mm = cv.moments(contour)
        cx = mm["m10"]/mm["m00"]
        cy = mm["m01"]/mm["m00"]  # 几何图形的中心位置 , mm是字典类型
        cv.circle(image, (np.int(cx), np.int(cy)), 2, (0, 255, 255), -1)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)  # 外接矩形
        print("contour area ", area)


def contours_find(image):
    dst = cv.GaussianBlur(image, (9, 9), 0)
    # dst = cv.bilateralFilter(image, 0, 30, 3)
    # dst = cv.pyrMeanShiftFiltering(image, 3, 30)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    thresh = cv.Canny(gray, 50, 150)          # 效果最好
    # ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 45, 10)
    cv.imshow("thresh image", thresh)
    # 得到修改后的轮廓，轮廓的层次
    contours, heriachy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)     # 绘制轮廓
        print(i)
    edge_measure(image, contours)
    cv.imshow("detect contours", image)


def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"http://image001.yambs.net/20170720/b2a9043ac1c6b1ecb142f3f84963f822.jpg")
# src = net_imread(r"http://vdposter.bdstatic.com/8473b01c20babbe0f0996c3a54fdf783.jpeg")
# src = net_imread(r"http://h.hiphotos.baidu.com/zhidao/pic/item/7acb0a46f21fbe09fc0c5d7068600c338744ad00.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
contours_find(src)
cv.waitKey(0)
cv.destroyAllWindows()
