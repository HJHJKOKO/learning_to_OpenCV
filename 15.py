import cv2 as cv
import numpy as np
# 15.模板匹配


def templeate_demo():
    # 要匹配的模板
    tpl = cv.imread("F:/0152.jpg") 
    # 要匹配的圖像
    target = cv.imread("F:/0153.jpg") 
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    # 模板匹配算法
    # methods = [cv.TM_SQDIFF, cv.TM_CCORR, cv.TM_CCOEFF] 
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED] 
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:  
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(target, tl, br, (0, 255, 0), 2)
        cv.imshow("match-" + np.str(md), target)
        # cv.imshow("match-" + np.str(md), result)
        # cv.imwrite("F:/match-"+np.str(md)+".jpg", target)

print("--------opencv python-------")
src = cv.imread("E:/007.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

templeate_demo()

cv.waitKey(0)

cv.destroyWindow()


