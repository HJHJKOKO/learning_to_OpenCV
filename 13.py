import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt
# 13.直方圖應用


# 直方圖均衡化
def equalHist_demo(image):
    # 都基於灰路圖像才能作均衡化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 局部自適應直方圖 可由參數調整對比度
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


def create_rgb_hist(image):
    h, w, c = image.shape
    # 這邊初始化 r 16, g 16, b 16 通道 1
    rgbHist = np.zeros([16*16*16, 1], np.float32)      
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            # 降維度
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1 
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    # 巴氏距離 趨近 0 越相似 
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)  
    # 相關性 趨近 1 越相似
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)         
    # 卡方 趨近 0 越相似
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)         
    print("巴氏距離: %s, 相關性: %s, 卡方: %s"%(match1, match2, match3))    


print("--------opencv python-------")
src = cv.imread("F:/rice.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("image", src)

# equalHist_demo(src)
# clahe_demo(src)

# 直方圖比較
image1 = cv.imread("F:/01.jpg")  
image2 = cv.imread("F:/01copy2.jpg")
cv.imshow("image1", image1)
cv.imshow("image2", image2)
hist_compare(image1, image2)

cv.waitKey(0)

cv.destroyWindow()