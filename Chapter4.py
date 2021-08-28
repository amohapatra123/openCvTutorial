# drawing shapes and writing text on image
import cv2
import numpy as np

# making a black background
# we can do that by taking a matrix of zeros as 0 are black in
img = np.zeros((600, 800, 3));
# setting the color
# img[:] = 250,0,0

# drawing a line
# line(image,starting point,ending point,color,thickness)
cv2.line(img, (0, 0), (400, 300), (0, 255, 0), 3);

# drawing a rectangle
cv2.rectangle(img,(400,300),(700,500),(0,255,0),3)
# to fill the shape instead of passing the thickness pass cv2.FILLED

# drawing a circle
# circle(img,center,radius,color,thickness)
cv2.circle(img,(550,400),100,(0,255,0),3)

# put text on image
cv2.putText(img,"openCV Tutorial",(400,280),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
cv2.imshow("Window", img)
cv2.waitKey(0)
