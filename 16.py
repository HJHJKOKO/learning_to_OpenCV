import numpy as np
import cv2 as cv
# 16.圖像二值化


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) 
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE) 
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    print("threshold value %s"%ret)
    cv.imshow("binary", binary)


def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # blockSize 為奇數，c 為常量 其他那個值減去均值10 才設為白色 or 黑色
    # binary1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    binary2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 5)
    # cv.imshow("binary1", binary1)    
    cv.imshow("binary2", binary2)
    cv.imwrite("F:/local_threshold_cat.jpg", binary2)

def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    # reshape 03課程有提到
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    print("mean:", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)

print("--------opencv python-------")
src = cv.imread("F:/Y0608.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# threshold_demo(src)
local_threshold(src)
# custom_threshold(src)
cv.waitKey(0)

cv.destroyWindow()
