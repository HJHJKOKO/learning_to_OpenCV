import cv2 as cv
import numpy as np
# 09.模糊操作


# 均值模糊
def blur_demo(image):
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo", dst)
    

# 中值模糊 處理圖像有些許 noise 噪點
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)

 
# 自定義模糊 捲積 kernel 銳化處理
def custom_blur_demo(image):
    # 最後除以25防止溢出
    # kernel = np.ones([5, 5], np.float32)/25
    # 提升圖像對比，數值設定為奇數 加總為 1 或 0
    kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)  
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)
    cv.imwrite("F:/kernel_chou_blur.jpg", dst)


print("---------hello python---------")
src = cv.imread("F:/333.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

# blur_demo(src)

# median_blur_demo(src)

custom_blur_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()
