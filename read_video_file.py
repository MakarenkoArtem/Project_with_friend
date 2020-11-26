import cv2

cap = cv2.VideoCapture('frame.mp4')
blue = cv2.VideoCapture('blue.avi')
red = cv2.VideoCapture('red.avi')
from time import sleep
while 1:
    ret, frame = cap.read()
    print(ret)
    if cv2.waitKey(1) == ord('q') or not ret:
        break
    cv2.imshow('frame', frame)
    ret, frame = blue.read()
    cv2.imshow('blue', frame)
    ret, frame = red.read()
    cv2.imshow('red', frame)
    sleep(0.02)
cap.release()
red.release()
blue.release()
cv2.destroyAllWindows()
