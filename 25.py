import cv2 as cv
# 25.膨脹與腐蝕


def erode_demo(image):
    print(image.shape)
    gray = cv. cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  
    cv.imshow("binary", binary)
    # 得到 結構元素 
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (6, 6))  
    dst = cv.erode(binary, kernel)                            
    cv.imshow("erode_demo", dst)


def dilate_demo(image):
    print(image.shape)
    gray = cv. cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  
    dst = cv.dilate(binary, kernel)                           
    cv.imshow("dilate_demo", dst)


print("-------hello python--------")
src = cv.imread("F:/cat/Y0608.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

# erode_demo(src)
# dilate_demo(src)
# 在此操作 erode  dilate 
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  
dst = cv.erode(src, kernel)                                       
cv.imshow("result", dst)                      
# cv.imwrite("F:/erode_cat.jpg", dst)
cv.waitKey(0)

cv.destoryAllWindows()