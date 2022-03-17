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
    show_and_nameWindow(img, windowName='ori_image')
    img_result = cv.filter2D(img, -1, kernel)
    show_and_nameWindow(img_result, 'result_img')
    img_result_L1 = cv.filter2D(img, -1, kernel_l1)
    show_and_nameWindow(img_result_L1,windowName='result_img_l1')

    cv.waitKey(0)

def laplacian_filter(img):

    gray_lap = cv.Laplacian(img, cv.CV_16S, ksize=5)
    img_laplacian = cv.convertScaleAbs(gray_lap)

    show_and_nameWindow(img, windowName='ori_image')
    show_and_nameWindow(img_laplacian, windowName='img_laplacian')
    cv.waitKey(0)

def main():
    img_ori = cv.imread("image/YuruCamp.jpg")
    #my_first_kernel(img_ori)
    laplacian_filter(img_ori)

if __name__ == "__main__":
    main()
