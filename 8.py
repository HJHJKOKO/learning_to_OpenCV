import cv2 as cv
import numpy as np
# 08.ROI 與 泛洪填充


def fill_color_demo(image):
    # copy 圖像
    copyImg = image.copy()
    h, w = image.shape[:2]  
    # 建立一個 MASK 參數要求如下                    
    mask = np.zeros([h+2, w+2], np.uint8) 
    # (0, 255, 255)表黃色    
    cv.floodFill(copyImg, mask, (30, 30), (255, 0, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)


def fill_binary():
    # 創建圖像
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, : ] = 255
    cv.imshow("fill_binary", image)
    # 創建 MASK 400+2, 400+2, 1(單通道)
    mask = np.ones([402, 402, 1], np.uint8) 
    mask[101:301, 101:301] = 0              
    cv.floodFill(image, mask, (200, 200), (255, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)

print("----------hello world----------")
src = cv.imread("F:/07.jpg")
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE) 
cv.imshow("input image", src)

fill_color_demo(src)
# fill_binary()

# ROI (Region of Interest) 操作
# 定義圖像的範圍
# face = src[10:220, 130:290]      
# 轉成灰階圖像
# gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# 再轉回'3'通道的圖像 才能合回'3'通道原圖
# backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# src[10:220, 130:290] = backface
# cv.imshow("face", backface)

cv.waitKey(0)

cv.destoryAllWindows()