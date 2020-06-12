import cv2 as cv
import numpy as np
# 06.像素運算01


def add_demo(m1, m2):
    # 將兩張圖 像素 相加
    dst = cv.add(m1,m2)             
    cv.imshow("add_demo", dst)


def substract_demo(m1, m2):    
    # 將兩張圖 像素 相減
    dst = cv.subtract(m1,m2)        
    cv.imshow("substract_demo", dst)


def divide_demo(m1, m2):
    # 將兩張圖 像素 相除
    dst = cv.divide(m1,m2)          
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
   # 將兩張圖 像素 相乘
    dst = cv.multiply(m1,m2)         
    cv.imshow("multiply_demo", dst)  


# def others(m1,m2):
#     # 計算均值 對每個通道求均值             
#     M1 = cv.mean(m1)
#     M2 = cv.mean(m2)
#     print(M1)
#     print(M2)


def others(m1,m2):
    # 計算方差 使用 meanStdDev               
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m2.shape[:2]
    
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)
    # 抓取 m2 的 h, w 值計算 均值與方差
    img = np.zeros([h,w], np.uint8)      
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)                 

print("------------hello world----------")
# 輸入兩張圖像並打印出圖像與 shape
src1 = cv.imread("F:/001.jpg")
src2 = cv.imread("F:/002.jpg") 
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE) 
cv.imshow("image1", src1)
cv.imshow("image2", src2)

# add_demo(src1, src2)
# substract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
others(src1, src2)

cv.waitKey(0)

cv.destoryAllWindows()