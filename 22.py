import cv2 as cv
import numpy as np
# 22.霍夫變換圓檢測


def detext_circles_demo(image):
    # 對應之前11章所用的均值遷移模糊功能
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    # cv.imshow("Filter", dst)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # cv.imshow("gray", cimage)
    # 霍夫圓檢測
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 30, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        # 畫圓心
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("Hough_circles", image)

print("-------hello python--------")
src = cv.imread("F:/coins.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
detext_circles_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()