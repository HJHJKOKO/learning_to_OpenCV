import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 14.直方圖反向投影


def back_projection_demo():
    sample = cv.imread("F:/0141.jpg")
    target = cv.imread("F:/014.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show image
    cv.imshow("sample", sample)
    cv.imshow("target", target)

    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [16, 16], [0, 180, 0, 256])
    # 圖像歸一化
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow("back_projection_demo", dst)
    # 小作業 將圖像非操作
    mask = cv.bitwise_not(dst)       
    cv.imshow("inverse_demo", mask)


def hist2d_demo(image):
    # hsv = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    hist = cv.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256])  
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()

print("--------opencv python-------")
src = cv.imread("F:/01.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)

# hist2d_demo(src)
back_projection_demo()

cv.waitKey(0)

cv.destroyWindow()
