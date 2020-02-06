import cv2.cv2 as cv

def img_info(img):
    h = img.shape[0]    # 高
    w= img.shape[1]     # 宽
    c = img.shape[2]    # 通道
    print(w, h, c)
    print(img.shape)
    print(img.shape[:1])
    print(img.shape[:2])

def access_pixels(img):
    h = img.shape[0]
    w = img.shape[1]
    c = img.shape[2]
    for row in range(h):
        for col in range(w):
            for ch in range(c):
                pv = img[row, col, ch]
                img[row, col, ch] = 255 - pv
    cv.imshow("pixels img", img)

def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame


# src = cv.imread(r"C:\Users\Administrator\Pictures\ye.jpg")
src = net_imread(r"https://preview.qiantucdn.com/58pic/35/32/48/60Y58PICu92fF78h1va39_PIC2018.jpg!w1024_new_small")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
img_info(src)
# access_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()

