import numpy as np
import cv2 as cv
# 02.圖像加載與保存


# 定義一個 video 視訊鏡頭
def video_demo():                   
    capture = cv.VideoCapture(0)    
    while True:
        ret, frame = capture.read()
        # 使用 flip 把鏡頭左右對調
        frame = cv.flip(frame, 1)   
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        # ESC的意思
        if c == 27: 
            break


# 定義出 image 的各項資料
def get_image_info(image):          
    # 顯示 image 資料類型
    print(type(image))              
    # 顯示 image 高、寬、通道
    print(image.shape)              
    print(image.size) 
    # 顯示 image 類型          
    print(image.dtype)              
    pixel_data = np.array(image)    
    # 顯示 image array 的型態
    print(pixel_data)               
   
   
print("---------Hello opencv------")
cv.namedWindow("input image", cv.COLOR_BGR2GRAY)
src = cv.imread("F:/007.jpg")                 
cv.imshow("input_image", src)
# 定義一張灰階圖像
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  
# 顯示灰階圖像
cv.imshow("gray_img", gray_img)                 
# 保存 gray_img 輸入路徑 檔名 副檔名
cv.imwrite("F:/productions/2/gray_demo.jpg", gray_img)            

# 開啟視訊
# video_dome()
  
# 得到 圖像 的屬性資訊   
get_image_info(src)  

cv.waitKey(0)

cv.destoryAllWindows()
