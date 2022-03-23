import cv2
import numpy as np
import os

def NormalImg (path):
    img = cv2.imread(path)
    cv2.namedWindow("Normal", cv2.WINDOW_NORMAL)
    cv2.imshow("Normal", img)

def GettingCamera ():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("hsv", gray)
        lowerb = np.array([100])
        upperb = np.array([200])
        mask = cv2.inRange(gray, lowerb, upperb)
        result = cv2.bitwise_and(gray, gray, mask=mask)
        cv2.imshow("result", result)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


path = cv2.samples.findFile(os.path.join(os.getcwd(), 'image/YuruCamp.jpg'))
# os.getcwd() 當前程式執行路徑
NormalImg(path)
# GettingCamera()

if cv2.waitKey() == ord("c"):  # 按下C 就關閉所有視窗
    cv2.destroyAllWindows()


