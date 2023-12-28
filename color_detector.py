import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # kolor w formacie BGR (zakres koloru niebieskiego)
    lower = np.array([[[95, 0, 0]]], np.uint8)
    upper = np.array([[[255, 240, 200]]], np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('result', result)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
