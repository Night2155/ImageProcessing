import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

import ImageProcess
from ImageProcess import *

imgpath = "image\\fox_in_snow.jpg"
oriimg = cv.imread(imgpath)
imgCrop = oriimg[20:500, 20:500]
#gray = cv.cvtColor(oriimg, cv.COLOR_BGR2GRAY)
#cv.imshow("Thrsehold", ImageProcess.Thresholding(oriimg, 127))
#ImageProcess.Show_Histogram(gray)
#ImageProcess.Show_Histogram(oriimg)
cv.imshow("sdad", imgCrop)
cv.waitKey(0)

