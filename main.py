import cv2
import numpy as np
import os
from ImageProcess import Thresholding

imgpath = "image\\YuruCamp.jpg"
oriimg = cv2.imread(imgpath, cv2.IMREAD_COLOR)
img_after = cv2.cvtColor(oriimg, cv2.COLOR_BGR2GRAY)
#cv2.imshow("ori", oriimg)
#cv2.imshow("Gray", img_after)
thre = 127
Thresholding(img_after,200)
cv2.waitKey(0)

