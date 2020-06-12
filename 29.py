import cv2 as cv
import numpy as np
# 29.人臉偵測


def face_detect_demo():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("gray image", gray)
    # 檢測器
    eye_cascade = cv.CascadeClassifier("F:/haarcascade_eye.xml")
    face_detector = cv.CascadeClassifier("F:/haarcascade_frontalface_default.xml")     
    # face_detector = cv.CascadeClassifier("F:/lbpcascade_frontalcatface.xml")         
    # 後面兩個參數重要
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 15)
    for (x, y, w, h) in eyes:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1)
    faces = face_detector.detectMultiScale(gray, 1.02, 10)  
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("result", src)
    cv.imwrite("F:/292face.jpg", src)

print("-------hello python--------")
src = cv.imread("F:/29.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
cv.imshow("imput image", src)

# 定義一個視訊頭
# capture = cv.VideoCapture(0)
# while True:
#     ret, frame = capture.read()
#     frame = cv.flip(frame, 1)
#     face_detect_demo(frame)
#     c = cv.waitKey(10)
#     if c == 27: 
#         break

face_detect_demo()       

cv.waitKey(0)

cv.destoryAllWindows()