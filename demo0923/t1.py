import cv2
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', img)
K = cv2.waitKey(0)