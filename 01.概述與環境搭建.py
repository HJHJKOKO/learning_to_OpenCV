import cv2 as cv
# 01.概述與環境搭建


print("-------hello python--------")
# imread 指定圖像路徑 
src = cv.imread("F:/007.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
cv.waitKey(0)

cv.destoryAllWindows()
