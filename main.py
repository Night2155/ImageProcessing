import cv2
import numpy as np
import os

path = cv2.samples.findFile(os.path.join(os.getcwd(), '../YuruCamp.jpg'))
GrayImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("GrayImg", cv2.WINDOW_NORMAL)
cv2.imshow("GrayImg", GrayImg)
cv2.waitKey()
#img = cv2.imread(cv2.samples.findFile("YuruCamp.jpg"), cv2.IMREAD_COLOR)
#cv2.imshow("img", img)
#cv2.waitKey()
