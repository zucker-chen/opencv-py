import cv2.cv2 as cv
import numpy as np


def img_pixels_range(gray, max):
    h = gray.shape[0]
    w = gray.shape[1]
    print(w, h)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            # Y >= 255像素置0 (过曝像素)
            if pv >= 254:
                pv = 0
            pv = pv * max / 256


def img_fusion(img1, img2):
    print(img1.shape, img2.shape)
    # img1 = cv.resize(img1, (640, 480))
    # img2 = cv.resize(img2, (640, 480))
    # cv.imshow("img1", img1)
    print(img1.shape)
    # 分离YUV数据
    yuv1 = cv.cvtColor(img1, cv.COLOR_BGR2YCrCb)
    y1, u1, v1 = cv.split(yuv1)
    yuv2 = cv.cvtColor(img2, cv.COLOR_BGR2YCrCb)
    y2, u2, v2 = cv.split(yuv2)
    # cv.imshow("y1", y1)
    # cv.imshow("y2", y2)
    # Y值均衡化
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    y2 = clahe.apply(y2)
    # Y像素范围压缩
    img_pixels_range(y1, 128)
    img_pixels_range(y2, 128)
    cv.imshow("y1", y1)
    cv.imshow("y2", y2)
    # y3 = cv.add(y1, y2)
    y3 = cv.addWeighted(y1, 0.6, y2, 0.4, 0)
    cv.imshow("y3", y3)
    img3 = cv.merge([y3, u1, v1])
    img3 = cv.cvtColor(img3, cv.COLOR_YCrCb2BGR)
    cv.imshow("img3", img3)
    cv.imwrite(r".04-picture-fusion_images/opencv.jpg", img3)






img1 = cv.imread(r".04-picture-fusion_images/rgb.jpg")
img2 = cv.imread(r".04-picture-fusion_images/mono.jpg")
# cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
# cv.imshow("img1", img1)
# cv.imshow("img2", img2)
img_fusion(img1, img2)
cv.waitKey(0)
cv.destroyAllWindows()
