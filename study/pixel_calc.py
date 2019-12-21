import cv2.cv2 as cv







def net_imread(url):
    cap = cv.VideoCapture(url)
    ret, frame = cap.read()
    if ret == False:
        return False
    else:
        return frame

def img_add_weight(img, conrast, alpha):
    return cv.addWeighted(img, conrast, False, False, alpha)

def img_calc(img1, img2, method):
    if method == "add":
        return cv.add(img1, img2)
    elif method == "sub":
        return cv.subtract(img1, img2)
    elif method == "multi":
        return cv.multiply(img1, img2)
    elif method == "divide":
        return cv.divide(img1, img2)
    elif method == "and":
        return cv.bitwise_and(img1, img2)
    elif method == "or":
        return cv.bitwise_or(img1, img2)
    elif method == "not":
        return cv.bitwise_not(img1, img2)
    else:
        return False

# main
# cv.namedWindow("img1", cv.WINDOW_AUTOSIZE)
img1 = net_imread(r"https://preview.qiantucdn.com/58pic/35/37/40/39958PICAURJ1nS0vtJdN_PIC2018.jpg!w1024_new_small")
img2 = net_imread(r"https://preview.qiantucdn.com/58pic/35/27/86/77I58PIC458PICd9zdwdf5ueN_PIC2018.jpg!w1024_new_small")
cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("add", img_calc(img1, img2, "add"))
cv.imshow("multi", img_calc(img1, img2, "multi"))
cv.imshow("and", img_calc(img1, img2, "and"))
cv.imshow("add weight", img_add_weight(img1, 1.5, -100))

cv.waitKey(0)
cv.destroyAllWindows()

