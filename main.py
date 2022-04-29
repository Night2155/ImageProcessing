import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
import ImageProcess
from ImageProcess import *
from ClassFile import Image_20220317

imgpath = "image\\fox_in_snow.jpg"
oriimg = cv.imread(imgpath)
#Image_20220317.my_first_kernel(oriimg)
Image_20220317.gussian_filter(oriimg)
Image_20220317.median_filter(oriimg)
#Image_20220317.sobel_filter(oriimg)
#imgCrop = cv.cvtColor(oriimg, cv.COLOR_BGR2HSV)
#gray = cv.cvtColor(oriimg, cv.COLOR_BGR2GRAY)
#cv.imshow("Thrsehold", ImageProcess.Thresholding(oriimg, 127))
#ImageProcess.Show_Histogram(gray)
#ImageProcess.Show_Histogram(oriimg)
#cv.imshow("sdad", imgCrop)
cv.waitKey(0)


