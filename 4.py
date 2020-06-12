import numpy as np
import cv2 as cv
# 04.色彩空間轉換01


def color_space_demo(image):    
    # 灰階處理 
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   
    cv.imshow("gray", gray)
    # cv.imwrite("F:/productions/4/gray.jpg", gray)
    # 較常見互相轉換
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)     
    cv.imshow("hsv", hsv)
    # cv.imwrite("F:/productions/4/hsv.jpg", hsv)
    # 較常見互相轉換
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)     
    cv.imshow("yuv", yuv)
    # cv.imwrite("F:/productions/4/yuv.jpg", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)  
    cv.imshow("Ycrcb", Ycrcb)
    # cv.imwrite("F:/productions/4/Ycrcb.jpg", Ycrcb)


print("-----------hello world----------")
src = cv.imread("F:/03.jpg") 
cv.namedWindow("imput image", cv.WINDOW_AUTOSIZE)  
cv.imshow("image", src)
color_space_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()