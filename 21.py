import cv2 as cv
import numpy as np
# 21.霍夫直線變換介紹 Hough Line Transform


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 先求得到Canny邊緣
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    cv.imshow("edges_image", edges)
    lines = cv.HoughLines(edges, 1, np.pi/180, 250)
    for line in lines:
        print(type(lines))
        rho, theta = line[0]
        # 極座標的套用
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))  
        cv.line(image, (x1, y1), (x2, y2),(0, 0, 255), 2)
    cv.imshow("image-lines", image)

# possible表將有可能是直線的部分抓取
def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        print(type(lines))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2),(0, 0, 255), 2)
    cv.imshow("line_detect_possible_demo", image)

print("-------hello python--------")
src = cv.imread("F:/021.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
 
# line_detection(src)
line_detect_possible_demo(src)

cv.waitKey(0)

cv.destoryAllWindows()