import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 12.圖像直方圖 histogram


def polt_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方圖")


def image_hist(image):
    color = ('blue', 'green', 'red')
    # 使用枚舉 令 i 和 color 列舉值出來    
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

print("--------opencv python-------")
src = cv.imread("F:/03.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
# polt_demo(src)
image_hist(src)
cv.waitKey(0)

cv.destroyWindow()
