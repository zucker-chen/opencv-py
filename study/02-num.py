import numpy as np
import cv2.cv2 as cv

def create_img():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 255
    img[:, :, 1] = 255
    cv.imshow("image", img)


cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
create_img()
cv.waitKey(0)
cv.destroyAllWindows()
