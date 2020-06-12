import cv2 as cv
import numpy as np
# 27.其他形態學操作


def hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("black_hat1", dst)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst1 = cv.add(dst, cimage)
    cv.imshow("black_hat2", dst1)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)
    cv.imshow("hat_binary_demo", dst)


def gradient_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient_demo", dst)


def gradient2_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    # 膨脹
    dm = cv.dilate(image, kernel)
    # 腐蝕
    em = cv.erode(image, kernel)
    # internal gradient 內部梯度
    dst1 = cv.subtract(image, em)
    # external gradient 外部梯度
    dst2 = cv.subtract(dm, image)   
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


print("-------hello python--------")
src = cv.imread("F:/004.jpg")  
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

# hat_demo(src)
# hat_binary_demo(src)
# gradient_demo(src)
gradient2_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()