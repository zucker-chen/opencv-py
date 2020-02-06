import cv2.cv2 as cv
import numpy as np






def template_demo(target):
    tpl = target[287:313, 312:327, :3]               # 建筑门前石墩装饰
    cv.imshow("template_image", tpl)
    # cv2.imshow("target image", target)
    methods = [cv.TM_CCOEFF_NORMED, cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)       # tl[0] = x, tl[1] = y
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        if md == cv.TM_CCOEFF_NORMED:
            # 多对象模板匹配及绘制
            threshold = 0.6
            loc = np.where(result >= threshold)
            for pt in zip(*loc[::-1]):
                cv.rectangle(target, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 2)
        cv.imshow("match-" + np.str(md), target)
        # cv.imshow("result-" + np.str(md), result)


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
template_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
