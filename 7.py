import cv2 as cv
import numpy as np
# 07.邏輯運算02


def logic_demo(m1, m2):
    # 與 and 運算
    dst1 = cv.bitwise_and(m1, m2)
    # 或 or 運算   
    dst2 = cv.bitwise_or(m1, m2)
    cv.imshow("logic_and_demo", dst1)
    cv.imshow("logic_or_demo", dst2)  
    image = cv.imread("F:/002.jpg")
    # 非 not 運算 對應 第03課程 inverse 操作
    dst3 = cv.bitwise_not(image) 
    cv.imshow("logic_not_demo", dst3)


def constrast_brightness_demo(image, c, b):       
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    # addWeighted 調整 對比度 亮度
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)

# 計算方差值
def others(m1,m2):                 
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    
    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h,w], np.uint8)      
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


print("-------------hello world----------")
src1 = cv.imread("F:/001.jpg")
src2 = cv.imread("F:/002.jpg") 
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE) 
cv.imshow("image1", src1)
cv.imshow("image2", src2)

src = cv.imread("F:/005.jpg")
cv.imshow("image2", src)
# 參數 對比度, 亮度
# constrast_brightness_demo(src, 1.2, 0)


# logic_demo(src1, src2)
others(src1, src2)

cv.waitKey(0)
cv.destoryAllWindows()