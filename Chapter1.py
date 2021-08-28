import cv2

# importing and displaying video
img = cv2.imread("Resources/Anshuman.png");
cv2.imshow("Image Window", img);
cv2.waitKey(0);

# importing and displaying video
vid = cv2.VideoCapture("Resources/Video.mp4");
while True:
    success, img = vid.read();
    cv2.imshow("Video output", img);
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# using the webcam
# id for width is 3
# id for height is 4
webcam = cv2.VideoCapture(0);
webcam.set(3, 500);
webcam.set(4, 800);
webcam.set(10, 100);
while True:
    success, img = webcam.read();
    cv2.imshow("Webcam", img);
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
