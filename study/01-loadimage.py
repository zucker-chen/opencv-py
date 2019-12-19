import cv2.cv2 as cv

def img_info(img):
    h = img.shape[0]
    w = img.shape[1]
    c = img.shape[2]
    print(h, w, c)

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

src = cv.imread(r"C:\Users\Administrator\Pictures\ye.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
img_info(src)
access_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()

