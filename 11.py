import cv2 as cv
# 11.邊緣保留濾波EPF


def bi_demo(image):
    # 高斯雙邊模糊
    dst = cv.bilateralFilter(image, 0, 80, 15)    
    cv.imshow("bi_demo", dst)
    # cv.imwrite("F:/bi_cat.jpg", dst)

def shift_demo(image):
    # 均值遷移模糊
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)   
    cv.imshow("shift_demo", dst) 


print("-------python opencv-------")
src = cv.imread("F:/0608.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
print(src.shape)
cv.imshow("image", src)

# bi_demo(src)
shift_demo(src)

cv.waitKey(0)

cv.destroyWindow()