# 用opencv做直方图均衡

import cv2

img1 = cv2.imread('data/Fig0310(b)(washed_out_pollen_image).tif')

# 转灰度图再进行直方图均衡
gray_img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

# 直方图均衡化
hist_img = cv2.equalizeHist(gray_img)


cv2.imshow("gray", gray_img)
cv2.imshow('hist', hist_img)
K = cv2.waitKey(0)
