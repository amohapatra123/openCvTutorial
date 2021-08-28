# Learn important functions to be used
import cv2
import numpy as np

img = cv2.imread("Resources/Anshuman.png");

# converting into grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
cv2.imshow("Grayscale Image", imgGray);
cv2.waitKey(0);

# making the image blur
# the kernel number should be always odd number
imgBlur = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow("Blur Image", imgBlur);
cv2.waitKey(0);

# to find the edges in the image
# Canny edge detector
imgCanny = cv2.Canny(img,100,100);
cv2.imshow("Canny Image",imgCanny);
cv2.waitKey(0);

# image dilation
# make the edges thicker
# this would take a kernel
kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1);
cv2.imshow("Dilation Image",imgDilation);
cv2.waitKey(0);

# image erosion
# make the edges thinner
imgErode = cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgErode);
cv2.waitKey(0);
