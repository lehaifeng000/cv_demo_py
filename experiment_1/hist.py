import cv2
import matplotlib.pyplot as plt
import numpy as np


def hist(img: np.ndarray):
    """
    直方图均衡
    :param img: ndarray,二维矩阵，数值范围0~255
    :return: 直方图均衡化后的图像
    """
    from collections import Counter
    # 获取图片形状
    img_shape = img.shape
    # 获取像素点数量
    img_size = img.size
    transform = dict()
    # 变为1维向量好计算
    img_fla = img.flatten()
    # 计数
    counter = Counter(img_fla)
    s_k = 0.0
    # 计算每个灰度级转换的目标级数
    for i in range(256):
        r_k = 1.0 * i / 255
        n_k = counter[i]
        p_k = n_k / img_size
        s_k = s_k + p_k
        transform[i] = round(255 * s_k)
    # 创建和原图相同大小的矩阵用于存转换后的图像
    res = np.zeros(img_shape, dtype=float)
    # 灰度值转换
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            row_pix = img[i][j]
            new_pix = transform[row_pix]
            res[i][j] = new_pix
    # 返回直方图均衡化后的图像
    return res

# 读取图像
raw_img = cv2.imread('data/lena.jpg')
# cv2默认读取顺序为BGR，转为RGB(也可以直接BGR转GRAY)
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)
# 转为灰度图像
gray_img = cv2.cvtColor(raw_img, cv2.COLOR_RGB2GRAY)
# 直方图均衡化
hist_img = hist(gray_img)

# 以下为显示直方图均衡化前后的图像和直方图
plt.subplot(2, 2, 1)
plt.imshow(gray_img, cmap=plt.cm.gray)
plt.subplot(2, 2, 2)
plt.hist(gray_img.flatten(), range=(0, 256), bins=256)
plt.subplot(2, 2, 3)
plt.imshow(hist_img, cmap=plt.cm.gray)
plt.subplot(2, 2, 4)
plt.hist(hist_img.flatten(), range=(0, 256), bins=256)
# plt.savefig('result.png')
plt.show()

