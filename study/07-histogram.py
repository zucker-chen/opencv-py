import cv2.cv2 as cv
# import numpy as np
import matplotlib.pyplot as plt


def plot_demo(src):
    plt.hist(src.ravel(), 256, [0, 256])    # 直方图
    plt.xlim([0, 255])
    # plt.ylim([0, 10000])
    plt.xlabel('img bins')
    plt.show()


def image_hist_demo(image):
    color = {"blue", "green", "red"}
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据下标和数据，一般用在 for 循环当中。
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)         # 线
    plt.show()

# 全局直方图均衡化
def equal_hist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equal_hist_demo", dst)


# 局部直方图均衡化
def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGRA2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


# 直方图比较
def hist_compare(image1, image2):
    size = image1.shape[:2]
    image1 = cv.resize(image1, size)
    image2 = cv.resize(image2, size)
    image1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
    image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
    # image1 = cv.equalizeHist(image1)
    # image2 = cv.equalizeHist(image2)
    hist1 = cv.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv.calcHist([image2], [0], None, [256], [0, 256])
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    # 巴氏距离越小越相似，相关性越大越相似，卡方越大越不相似
    print("巴氏距离", match1)
    print("相关性", match2)
    print("卡方", match3)
    # 直方图绘制
    # 2-2-1
    plt.subplot(221)
    plt.imshow(image1, cmap=plt.cm.gray)
    # 2-2-3
    plt.subplot(223)
    plt.imshow(image2, cmap=plt.cm.gray)
    # 2-2-2
    plt.subplot(222)
    plt.plot(hist1)  # 线
    # 2-2-4
    plt.subplot(224)
    plt.plot(hist2)  # 线
    plt.show()


# 直方图反向投影
def back_projection_demo(target):
    sample = target[430:442, 305:317, :3]               # 建筑墙面色调块
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    cv.imshow("sample", sample)
    cv.imshow("target", target)
    roihist = cv.calcHist([roi_hsv], [0, 1], None, [8, 8], [0, 180, 0, 256])    # [180, 256] binsize小则查找粗糙
    cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)  # 归一化
    dst = cv.calcBackProject([target_hsv], [0, 1], roihist, [0, 180, 0, 256], 1)
    cv.imshow("backproject", dst)



def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"https://tuzhizhijia.com/uploads/allimg/180808/1535121527-0.jpg")
src1 = net_imread(r"http://n.sinaimg.cn/sinacn/w1000h750/20180310/9419-fxpwyhw7064094.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
# plot_demo(src)
# image_hist_demo(src)
# equal_hist_demo(src)
# clahe_demo(src)
hist_compare(src, src1)
back_projection_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
