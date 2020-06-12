import cv2 as cv
import numpy as np
# 19.圖像梯度


# sobel算子 一階導數(用於作邊緣偵測) 
def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    # Scharr 算子是 Soble算子的增強
    # grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    # grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)  
    # convertScaleAbs 轉絕對值 
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", grad_x)
    cv.imshow("gradient-y", grad_y)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


# 拉普拉斯算子 二維導數
def lapalian_demo(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    # cv.imshow("lapalian_demo", lpls)
    
    # 定義拉普拉斯算子
    # kernel_1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # dst1 = cv.filter2D(image, cv.CV_32F, kernel=kernel_1)
    # lpls_1 = cv.convertScaleAbs(dst1)
    # cv.imshow("lapalian_demo_1", lpls_1)
    
    kernel_2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst2 = cv.filter2D(image, cv.CV_32F, kernel=kernel_2)
    lpls_2 = cv.convertScaleAbs(dst2)
    cv.imshow("lapalian_demo_2", lpls_2)
   

print("-------hello python--------")
src = cv.imread("F:/037.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

sobel_demo(src)
# lapalian_demo(src)
cv.waitKey(0)

cv.destoryAllWindows()