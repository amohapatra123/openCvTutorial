import cv2

img = cv2.imread("Resources/Anshuman.png");

# Resize an image
# for resizing width first the height
imgResize = cv2.resize(img,(300,300));
cv2.imshow("Resized image",imgResize);
cv2.waitKey(0);

# cropping an image
# for cropping an image height first the width
imgCrop = img[10:200,40:200];
cv2.imshow("Cropped image",imgCrop);
cv2.waitKey(0);
