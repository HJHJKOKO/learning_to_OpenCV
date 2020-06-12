import cv2 as cv
import numpy as np
# 17.超大圖像二值化 


# def big_image_binary(image):
#     print(image.shape)
#     cw = 256
#     ch = 256
#     h, w = image.shape[:2]
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     for row in range(0, h, ch):
#         for col in range(0, w, cw):
#             roi = gray[row:row + ch, col:col + cw]
#             ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#             gray[row:row + ch, col:col + cw] = dst
#             print(np.std(dst), np.mean(dst))
#     cv.imwrite("F:/0177.jpg", gray)


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row + ch, col:col + cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("F:/0178.jpg", gray)


# def big_image_binary(image):
#         print(image.shape)
#         cw = 256
#         ch = 256
#         h, w = image.shape[:2]
#         gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#         for row in range(0, h, ch):
#             for col in range(0, w, cw):
#                 roi = gray[row:row+ch, col:col+cw]
#                 print(np.std(roi), np.mean(roi))
#                 dev = np.std(roi)
#                 # 設定要過濾的方差值
#                 if dev < 1:  
#                     # 此區域全部填上 255 黑色
#                     gray[row:row + ch, col:cw + col] = 255
#                 else:
#                     ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#                     gray[row:row + ch, col:col + cw] = dst
#             cv.imwrite("F:/0178.jpg", gray)


print("-------hello python--------")
src = cv.imread("F:/321.jpg")    
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("image", src)
big_image_binary(src)
cv.waitKey(0)

cv.destoryAllWindows()