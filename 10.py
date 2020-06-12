import cv2 as cv
import numpy as np
# 10.高斯模糊


# 設置 clamp if 255 else 0 
def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gauessian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            # blue
            b = image[row, col, 0]
            # green  
            g = image[row, col, 1]
            # red  
            r = image[row, col, 2]  
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image", image)
    # cv.imwrite("F:/noise_cat.jpg", image)


print("---------hello--------")
src = cv.imread("F:/0608.jpg")    
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

t1 = cv.getTickCount()
gauessian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time consume : %s ms" %(time*1000))

# 高斯模糊 參數 sigmaX 需用到數學原理
dst = cv.GaussianBlur(src, (5, 5), 0)     
cv.imshow("Gaussian Blur", dst)

cv.waitKey(0)

cv.destoryAllWindows()