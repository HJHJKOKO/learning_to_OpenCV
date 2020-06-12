import cv2 as cv
import numpy as np 

def watershed_demo():
    # remove noise if any    
    print(src.shape)
    # EPF 的均值遷移模糊
    blurrd = cv.pyrMeanShiftFiltering(src, 50, 100)
    # gray\binary image
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU )
    cv.imshow("binary-image", binary)


    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    # 膨脹操作
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt", sure_bg)


    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.02, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed tronsform 分水嶺變換
    markers = markers + 1
    # 像素操作
    markers[unknown == 255] = 0   
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("watershed", src)

print("-------Python OpenCV--------")
src = cv.imread("F:/07.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
watershed_demo()

cv.waitKey(0)

cv.destoryAllWindows()