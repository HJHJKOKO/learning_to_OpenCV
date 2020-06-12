import cv2 as cv
import numpy as np
# 26.開閉操作


def open_demo(image):
    print(image.shape)
    gray = cv. cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (35, 1))    
    # morphology 形態學 MORPH_OPEN 開操作
    binary_open = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)         
    cv.imshow("open-result", binary_open)


def close_demo(image):
    print(image.shape)
    gray = cv. cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    # morphology 形態學 MORPH_CLOSE 閉操作
    binary_close = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)      
    cv.imshow("close-result", binary_close)



print("-------hello python--------")
src = cv.imread("F:/026.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

open_demo(src)
# close_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()
