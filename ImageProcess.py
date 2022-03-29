import cv2 as cv
import matplotlib.pyplot as plt

def GrayImg(oriimg):
    grayimg = cv.cvtColor(oriimg, cv.COLOR_RGB2GRAY)
    return grayimg

def Thresholding(oriimg,thresh):
    oriimg = cv.cvtColor(oriimg, cv.COLOR_BGR2GRAY)
    ret, img_Thre = cv.threshold(oriimg, thresh, 255, cv.THRESH_BINARY)
    return img_Thre

def Histogram(oriimg):
    oriimg = cv.cvtColor(oriimg, cv.COLOR_RGB2GRAY)
    img_hist = cv.equalizeHist(oriimg)
    return img_hist

def Show_Histogram(oriimg):
    if len(oriimg.shape) == 3:
        color = ('b', 'g', 'r')
        alpha = (0.6, 0.6, 0.5)
        for i, col in enumerate(color):
            hist_graphic = cv.calcHist([oriimg], [i], None, [256], [0, 256])
            plt.bar(range(0, 256), hist_graphic.ravel(), color=color[i], alpha=alpha[i])
        plt.title("RGB Histogram")
        plt.show()
    else:
        color = 'gray'
        alpha = 0.6
        hist_graphic = cv.calcHist([oriimg], [0], None, [256], [0, 256])
        bar = plt.bar(range(0, 256), hist_graphic.ravel(), color=color, alpha=alpha)
        print(bar)
        plt.title("Gray Histogram")
        plt.show()

