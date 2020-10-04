import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite("test.jpg", gray_img)
cv2.imshow('image', gray_img)
K = cv2.waitKey(0)
