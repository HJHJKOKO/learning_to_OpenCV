import cv2 as cv
import numpy as np
# 20.Canny邊緣檢測


def Canny_edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)   
    gray =cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # 求 X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # 求 y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # 求 edge threshold1:threshold2 應為 1:3 or 1:2
    edge_output = cv.Canny(xgrad, ygrad, 50,  100)
    # edge_output = cv.Canny(gray, 50,  150)
    cv.imshow("Canny Eage", edge_output)

    # 彩色邊緣提取
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Color Edge", dst)

print("-------hello python--------")
src = cv.imread("F:/037.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
Canny_edge_demo(src)
cv.waitKey(0)

cv.destoryAllWindows()