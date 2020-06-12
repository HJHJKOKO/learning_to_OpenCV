import cv2 as cv
import numpy as np
# 23.輪廓發現


# 使用 Canny邊緣檢測方法
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (1, 1), 0)   
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # edge_output = cv.Canny(xgrad, ygrad, 30,  100)
    # 參數可以控制
    edge_output = cv.Canny(gray, 30, 100)        
    cv.imshow("Canny Eage", edge_output)
    return edge_output

def contours_demo(image):
    '''
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE) 
    cv.imshow("binary1_image", binary)'''
    Canny_edge = edge_demo(image)

    contours, heriachy = cv.findContours(Canny_edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) 
    for i, contour in enumerate(contours):
        # color 輸入-1可以填充
        cv.drawContours(image, contours, i, (255, 0, 0), -1)  
        print(i)
    cv.imshow("detect_contours1", image)

print("--------hello opencv---------")
src = cv.imread("F:/sample.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
contours_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()