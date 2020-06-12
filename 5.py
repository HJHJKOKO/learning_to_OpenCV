import numpy as np
import cv2 as cv
# 05.色彩空間轉換02


def extrace_object_demo():
    capture = cv.VideoCapture("F:/KICK.mp4")
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        # 轉成 hsv 色彩空間
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 辨識顏色 列表中的數值要參考表格 min 和 max 6個值 去輸入
        lower_hsv = np.array([156, 43, 46])               
        upper_hsv = np.array([180, 255, 255])
        # 使用 inRange 
        img = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        # 產生 MASK 遮罩 抓取顏色 對應 07課程
        dst = cv.bitwise_and(frame, frame, mask = img)  
        cv.imshow("video", frame)
        cv.imshow("mask", dst)
        c = cv.waitKey(30)
        if c == 27: 
            break

print("-----------hello world----------")
src = cv.imread("F:/05.jpg") 
cv.namedWindow("imput image", cv.WINDOW_AUTOSIZE)  
cv.imshow("image", src)

# extrace_object_demo()   

# 分離 b g r 三個通道
b, g, r = cv.split(src)     
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)


# 通道的分離與合併
src[:, :, 1] = 0  
# 利用 merge 合併 b g r           
# src = cv.merge([b, g, r])
cv.imshow("changed image", src)          

cv.waitKey(0)
cv.destoryAllWindows()