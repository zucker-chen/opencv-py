import cv2.cv2 as cv
import numpy as np



def fill_color_demo(image):
    copyIma = image.copy()
    h, w = image.shape[:2]
    print(h, w)
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyIma, mask, (30, 30), (0, 255, 255), (50, 50, 50), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    # cv.floodFill(copyIma, mask, (30, 30), (0, 255, 255), (20, 20, 10), (20, 20, 20))
    cv.imshow("fill_color", copyIma)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[50:350, 50:350, : ] = [0, 255, 0]
    image[100:300, 100:300, : ] = 255
    cv.imshow("fill_binary", image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[60:340, 60:340] = 0    # this range will be flood filled
    cv.floodFill(image, mask, (60, 60), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)



def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


src = net_imread(r"https://preview.qiantucdn.com/58pic/35/32/48/60Y58PICu92fF78h1va39_PIC2018.jpg!w1024_new_small")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

fill_binary()
fill_color_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()

'''
总结：
    1，mask，掩码参数：单通道，8bit，长和宽上都比输入图像 image 大2像素点的图像
    2，mask 中与输入图像(x,y)像素点相对应的点的坐标为(x+1,y+1)
    3，填充时不会填充掩膜mask的非零像素区域
    4，漫水填充法是一种用特定的颜色填充联通区域，通过设置可连通像素的上下限以及连通方式来达到不同的填充效果的方法
'''