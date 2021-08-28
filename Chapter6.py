# joining images
import cv2
import numpy as np

img = cv2.imread("Resources/Anshuman.png");

# horizontally stack images
imgHor = np.hstack((img,img));
cv2.imshow("Horizontal Stack",imgHor);
cv2.waitKey(0);

# vertical stack images
imgVer = np.vstack((img,img));
cv2.imshow("Vertical Stack",imgVer);
cv2.waitKey(0)