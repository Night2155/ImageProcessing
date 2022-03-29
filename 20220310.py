import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def image_contrast_enhance_gray(img, gamma):
    new_image = np.zeros(img.shape, dtype=img.dtype)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # alpha = 1.0
    # beta = 50

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            # new_image[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)
            new_image[y, x] = np.clip(pow(img[y, x]/255, 1 / gamma) * 255, 0, 255)
    cv.namedWindow("Contrast enhanced", cv.WINDOW_NORMAL)
    cv.imshow("Contrast enhanced", new_image)

def image_contrast_enhance_gray_easy(img, gamma, c):
    out = img.copy()
    out /= 255.
    out = (1/c * out) ** (1/gamma)
    out *= 255
    out = out.astype(np.uint8)
    cv.namedWindow("Gamma img easy", cv.WINDOW_NORMAL)
    cv.imshow("Gamma img easy", out)

def show_color_histo(img):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()

def show_histogram_with_subplot(img):
    cv.imshow('original gray image',img)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:300, 200:500] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])

    #plt.subplot(2, 2, 1)
    #plt.imshow(img)
    plt.subplot(2, 2, 2)
    plt.imshow(mask)
    plt.subplot(2, 2, 3)
    plt.imshow(masked_img)
    plt.subplot(2, 2, 4)
    plt.plot(hist_full)
    plt.subplot(2, 2, 4)
    plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()

path = "image\\triodoshippo_heroImageFullWidthMobile.jpg"
img = cv.imread(path)

GrayImgori = cv.imread(path, cv.IMREAD_GRAYSCALE)
#cv.namedWindow("ori", cv.WINDOW_NORMAL)
#cv.imshow("ori", img)
#cv.imshow('Gray ori', GrayImgori)
#image_contrast_enhance_gray(img, gamma=5)
#image_contrast_enhance_gray_easy(GrayImgori.astype(np.float), gamma=5, c=1)
show_color_histo(img)
show_histogram_with_subplot(GrayImgori)
cv.waitKey()