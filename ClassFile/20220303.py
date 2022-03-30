import cv2 as cv
import numpy as np
# 讀取靜態影像檔
# img = cv.imread('image/1233.png')
# 轉換色彩空間

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 顯示影像

# cv.imshow('image', img)
# cv.imshow('gray', gray)
# 影像存檔

# cv.imwrite('image/gray.png', gray)
# 列印影像尺寸

# print(img.shape)

cap = cv.VideoCapture(0)
while True:
    # 取得camera的連續影像
    ret, frame = cap.read()
    # 將靜態的frame轉換成灰階影像
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 顯示原始影像與灰階影像
    cv.imshow('frame', frame)
    frame50 = frame + 50;
    cv.imshow('frame + 50', frame50)
    # cv.imshow('gray image', gray)
    # 定義影像ROI (region of interest)
    # roi = frame[100:400, 200:550]
    # roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    # cv.imshow('ROI gray', roi_gray)
    # roi_ret, roi_mask = cv.threshold(roi_gray, 100, 200, cv.THRESH_BINARY)
    # roi_mask_inv = cv.bitwise_not(roi_mask)
    # cv.imshow('ROI mask', roi_mask_inv)
    # 定義lower-bound, upper-bound
    lowerb = np.array([100])
    upperb = np.array([200])
    mask = cv.inRange(gray, lowerb, upperb)
    result = cv.bitwise_and(gray, gray, mask = mask)
    # 顯示過濾後的結果影像
    cv.imshow('result', result)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()