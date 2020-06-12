import cv2 as cv
# 18.圖像金字塔


# 高斯金字塔
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):  
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down" +str(i), dst)
        temp = dst.copy()
    return pyramid_images


# 拉普拉斯 圖像 金字塔
def lapalian_demo(image):
    # 接收高斯金塔的值 pyramid_images
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        #  為了得到原圖 else 對原圖處理
        if (i-1) < 0: 
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_"+str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapalian_down_"+str(i), lpls)

print("-------hello python--------")
src = cv.imread("F:/0608.jpg")   
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)

pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)

cv.destoryAllWindows()
