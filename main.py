import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

import ImageProcess
from ImageProcess import *

imgpath = "image\\YuruCamp.jpg"
oriimg = cv2.imread(imgpath)
imgCrop = oriimg[20:500, 20:500]
gray = cv.cvtColor(oriimg, cv2.COLOR_RGB2GRAY)
#cv.imshow("Gray", ImageProcess.GrayImg(oriimg))
#cv.imshow("Hist", ImageProcess.Histogram(oriimg))
#cv.imshow("Thrsehold", ImageProcess.Thresholding(oriimg, 127))
#ImageProcess.Show_Histogram(gray)
#ImageProcess.Show_Histogram(oriimg)
cv.imshow("sdad", imgCrop)
cv2.waitKey(0)

