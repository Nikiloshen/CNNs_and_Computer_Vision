import cv2
import mediapipe as mp
import time
import HandTrackingModule as HTM

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = HTM.HandDetector()

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img)
    if len(lm_list) != 0:
        print(lm_list[0])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)