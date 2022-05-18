import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from Function import Functions
class ImageProcess():

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

    def HSV(oriimg):
        HSVimg = cv.cvtColor(oriimg, cv.COLOR_BGR2HSV)
        return HSVimg

    def Gaussion(oriimg, kernelsize, value):
        Gaussionimg = cv.GaussianBlur(oriimg, (kernelsize, kernelsize), value)
        return Gaussionimg

    def Median(oriimg, kernelsize, value):
        MedianImg = cv.medianBlur(oriimg, kernelsize, value)
        return MedianImg

    def Canny(oriimg, Max, Min):
        CannyImg = cv.Canny(oriimg, threshold1=int(Min), threshold2=int(Max))
        return CannyImg

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
            plt.figure()
            bar = plt.bar(range(0, 256), hist_graphic.ravel(), color=color, alpha=alpha)
            print(bar)
            plt.title("Gray Histogram")
            plt.show()

    def Show_ROI_Image(img, TY, DY, LX, RX):
        ROI_image = img[int(TY):int(DY), int(LX):int(RX)]
        ROI_image = cv.cvtColor(ROI_image, cv.COLOR_BGR2RGB)
        plt.axis('off')
        plt.imshow(ROI_image)
        plt.show()

    def Show_Perspective_Image(image, points):
        width, height = image.shape[:2]
        pts1 = np.float32(points)
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        m = cv.getPerspectiveTransform(pts1, pts2)
        PerspectiveImg = cv.warpPerspective(image, m, (width, height), cv.INTER_LINEAR)
        PerspectiveImg = cv.cvtColor(PerspectiveImg, cv.COLOR_BGR2RGB)
        plt.axis('off')
        plt.imshow(PerspectiveImg)
        plt.show()

    def Change_Angel_Image(oriimage, angel, turn_img):
        height, width = oriimage.shape[:2]
        center = (width / 2, height / 2)
        scale = 1.0
        # center = 影像中心點 angel = 旋轉角度 scale = 縮放比例
        AngelArray = cv.getRotationMatrix2D(center, int(angel), scale)
        turnimg = cv.warpAffine(turn_img, AngelArray, (width, height))
        return turnimg

    def Move_Image(oriimg, ImgMove, x, y):
        height, width = oriimg.shape[:2]
        # x = x軸偏移量 y = y軸偏移量
        MoveArray = np.float32([[1, 0, x], [0, 1, y]])
        MoveImg = cv.warpAffine(ImgMove, MoveArray, (width, height))
        return MoveImg