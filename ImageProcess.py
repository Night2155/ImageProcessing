import cv2 as cv

def Thresholding(oriimg,thresh):
    ret, img_Thre = cv.threshold(oriimg,thresh,255,cv.THRESH_BINARY)
    cv.imshow('img_Threhold',img_Thre)