import cv2.cv2 as cv


# Sobel算子
def sobel_gradient(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)           # 对x求一阶导
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)           # 对y求一阶导
    gradx = cv.convertScaleAbs(grad_x)                  # 用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv.convertScaleAbs(grad_y)
    # cv.imshow("sobel_x", gradx)                         # x方向上的梯度
    # cv.imshow("sobel_y", grady)                         # y方向上的梯度
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)  # 图片融合
    cv.imshow("sobel", gradxy)


# Scharr算子(Sobel算子的增强版，效果更突出)
def scharr_gradient(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)      # 对x求一阶导
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)      # 对y求一阶导
    gradx = cv.convertScaleAbs(grad_x)              # 用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv.convertScaleAbs(grad_y)
    # cv.imshow("scharr_x", gradx)                    # x方向上的梯度
    # cv.imshow("scharr_y", grady)                    # y方向上的梯度
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("scharr", gradxy)


# 拉普拉斯算子
def laplace_gradient(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("laplace", lpls)


# Canny边缘提取
def canny_edge(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) #x方向梯度
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1) #y方向梯度
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    # edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask= edge_output)
    cv.imshow("Color Edge", dst)


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
sobel_gradient(src)
scharr_gradient(src)
laplace_gradient(src)
canny_edge(src)
cv.waitKey(0)
cv.destroyAllWindows()
