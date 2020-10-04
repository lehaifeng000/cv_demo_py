# 合并两张图片
import cv2

img1 = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('fox.png', cv2.IMREAD_COLOR)

img1 = cv2.resize(img1, (128, 128))
img2 = cv2.resize(img2, (128, 128))

'''
参数：图像1，不透明度1,,图像2,,不透明度2,gamma
'''
im3 = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
cv2.imshow('合并', im3)
K = cv2.waitKey(0)
