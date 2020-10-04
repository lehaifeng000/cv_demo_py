# 贴图

import cv2

img1 = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('fox.png', cv2.IMREAD_COLOR)

size1 = (128, 128)
size2 = (32, 32)
img1 = cv2.resize(img1, size1)
img2 = cv2.resize(img2, size2)
# 从原图扣一部分，大小与小图相同
img_reg = img1[:size2[0], :size2[0]]
# 和小图片合并
img_3 = cv2.addWeighted(img2, 0.6, img_reg, 0.8, 0)
# 需要展示的图片，复制大图
img4 = img1
# 把大图的一部分改为合并好的小图
img4[:size2[0], :size2[0]] = img_3
# 显示图片
cv2.imshow('3', img4)

K = cv2.waitKey(0)