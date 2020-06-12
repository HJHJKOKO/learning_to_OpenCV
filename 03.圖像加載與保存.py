import cv2 as cv
import numpy as np
# 03.圖像加載與保存


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s" %(width, height, channels))
    for row in range(height):   
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)
    # cv.imwrite("F:/productions/3/pixels_demo.jpg", image)


def inverse(image):       
    # bitwise 對圖像進行二值 非 操作    
    dst = cv.bitwise_not(image)       
    cv.imshow("inverse_demo", dst)
    # cv.imwrite("F:/productions/3/inverse.jpg", dst)


def create_image():
    '''
    # 自定義 height width channels 類型 的圖像
    img_1 = np.zeros([500, 400, 3], np.uint8)  
    img_2 = np.zeros([500, 600, 3], np.uint8)
    img_3 = np.zeros([400, 1000, 3], np.uint8)
    img_1[:, :, 0] = np.ones([500, 400])*255
    img_2[:, :, 1] = np.ones([500, 600])*255
    img_3[:, :, 2] = np.ones([400, 1000])*255
    cv.imshow("new image1", img_1)
    cv.imshow("new image2", img_2)
    cv.imshow("new image3", img_3)
    # cv.imwrite("F:/productions/3/blue.jpg", img_1)    
    # cv.imwrite("F:/productions/3/green.jpg", img_2)
    # cv.imwrite("F:/productions/3/red.jpg", img_3)
    '''
    # 創立一張單通道圖像 0為黑色，127灰色，255白色  
    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0]= np.ones([400, 400])*127
    cv.imshow("new_image", img)
    # 直接存取寫入
    # cv.imwrite("F:/productions/3/single_white.jpg", img)    
        
    # 三維數列  np.float, unit8, int32
    # m1 = np.ones([3, 3], np.float32)
    # m1 = np.ones([3, 3], np.int32) 
    m1 = np.ones([3, 3], np.uint8)
    m1.fill(12222.388)               
    print(m1)
    
    # 變成一列
    m2 = m1.reshape([1, 9])          
    print(m2)
    
    # 自訂三維數組
    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.int32)   
    m3.fill(9)
    print(m3)


print("----------Hello Python------------")
# 三通道 bule green red
src= cv.imread("F:/01.jpg") 
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
# t1 數據
t1 = cv.getTickCount()         
# access_pixels(src)
# inverse(src)           
create_image()
# t2 數據
t2 = cv.getTickCount()         
time = (t2-t1)/cv.getTickFrequency()
# 計算時間 毫秒
print("time: %s ms" %(time*1000))        

cv.waitKey(0)

cv.destoryAllWindows()
