import numpy as np
import matplotlib.pyplot as plt
import cv2

a = [1, 9, 9, 9, 9, 9, 30]
aaa=np.array(a)
b = cv2.equalizeHist(aaa)
plt.subplot(1, 2, 1)
plt.hist(a)
plt.subplot(1, 2, 2)
plt.hist(b)
plt.show()
