import cv2 as cv
import numpy as np

def show_and_nameWindow(img,windowName):
    cv.namedWindow(windowName, cv.WINDOW_NORMAL)
    cv.imshow(windowName, img)

def my_first_kernel(img):
    # 平滑濾波 依照矩陣大小去調整 除數
    kernel = (np.ones((5, 5), np.float32)) / 25
    # kernel = (np.ones([[1,1,1],[1,1,1],[1,1,1]]), np.float.32) / 9
    # 邊緣擷取
    kernel_l1 = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ])

    kernel_l2 = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    img_result = cv.filter2D(img, -1, kernel)
    img_result_L1 = cv.filter2D(img, -1, kernel_l1)
    img_result_L2 = cv.filter2D(img, -1, kernel_l2)
    show_and_nameWindow(img, windowName='ori_image')
    show_and_nameWindow(img_result, 'result_img')
    show_and_nameWindow(img_result_L1,windowName='result_img_l1')
    show_and_nameWindow(img_result_L2, windowName='result_img_l2')

    cv.waitKey(0)

def averaging_filter(img):
    #show_and_nameWindow(img, windowName='ori_img')
    img_averag = cv.blur(img, (5, 5))
    show_and_nameWindow(img_averag, windowName='img_average')


def median_filter(img):
    img_median = cv.medianBlur(img, 7)
    show_and_nameWindow(img_median, windowName='img_median')


def laplacian_filter(img):
    gray_lap = cv.Laplacian(img, cv.CV_16S, ksize=5)
    img_laplacian = cv.convertScaleAbs(gray_lap)
    show_and_nameWindow(img, windowName='ori_image')
    show_and_nameWindow(img_laplacian, windowName='img_laplacian')

def gussian_filter(img):
    img_gussican_blur = cv.GaussianBlur(img, (11, 11), -1)
    show_and_nameWindow(img_gussican_blur, windowName='img_Guassican')

def sobel_filter(img):
    x = cv.Sobel(img, cv.CV_16S, 1, 0)
    y = cv.Sobel(img, cv.CV_16S, 0, 1)
    abs_x = cv.convertScaleAbs(x)
    abs_y = cv.convertScaleAbs(y)
    img_sobel = cv.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    show_and_nameWindow(abs_x, 'sobel_x')
    show_and_nameWindow(abs_y, 'sobel_y')
    show_and_nameWindow(img_sobel, 'img_sobel')

def add_gussian_noise(img):
    img = img / 255
    mean = 0
    sigma = 0.1
    noise = np.random.normal(mean, sigma, img.shape)
    img_gassian = img + noise
    img_gassian = np.clip(img_gassian, 0, 1)
    img_gassian = np.uint8(img_gassian * 255)
    noise = np.uint8(noise * 255)
    img_result = cv.fastNlMeansDenoising(img_gassian, None, 10, 10, 7)
    show_and_nameWindow(noise, 'noise')
    show_and_nameWindow(img_gassian, 'img_gaussian_noise')
    show_and_nameWindow(img_result, 'img_noise_result')

def main():
    img_ori = cv.imread("image/YuruCamp.jpg")
    show_and_nameWindow(img_ori, "img_ori")
    #my_first_kernel(img_ori)
    #laplacian_filter(img_ori)
    #averaging_filter(img_ori)
    #median_filter(img_ori)
    #gussian_filter(img_ori)
    #sobel_filter(img_ori)
    add_gussian_noise(img_ori)

    cv.waitKey(0)

if __name__ == "__main__":
    main()
