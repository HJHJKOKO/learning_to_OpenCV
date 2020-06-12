import cv2 as cv
import numpy as np 
# 24.對象測量


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  
    print("threshold value : %s"%ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)

    # 步驟1.使用輪廓發現
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h)/max(w, h)
        print("rectangle rate : %s"%rate)
        mm = cv.moments(contour)      
        print(type(mm))
        # 得到中心點，浮點數不可以除以零
        cx = mm['m10']/mm['m00']    
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area %s"%area)
        # 多邊形擬合求接近的輪廓
        approxCuve = cv.approxPolyDP(contour, 4, True)
        print(approxCuve.shape)
        # 抓取圓形用綠色
        if approxCuve.shape[0] > 6:                             
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)   
        # 抓取矩形用紅色
        if approxCuve.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        # 抓取三角形用藍色
        if approxCuve.shape[0] == 3:
            cv.drawContours(dst, contours, i, (255, 0, 0), 2)
    cv.imshow("measure-contours", dst)

print("---------hello python----------")
# 此部分選圖要注意黑白要分明
src = cv.imread("F:/sample2.jpg")           
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

measure_object(src)
cv.waitKey(0)

cv.destoryAllWindows()