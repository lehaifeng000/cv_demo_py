from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

import cv2

img1 = cv2.imread('data/Fig0310(b)(washed_out_pollen_image).tif')

# 转灰度图再进行直方图均衡
gray_img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

# 直方图均衡化
hist_img = cv2.equalizeHist(gray_img)

x = [s for s in range(10)]
plt.subplot(2, 1, 1)
aaa=gray_img.flatten()
plt.hist(gray_img.flatten(), range=(0, 256), bins=256)
plt.subplot(2, 1, 2)
plt.hist(hist_img.flatten(), range=(0, 256), bins=256)

# plt.plot(count.keys(),count.values(),)
plt.show()
