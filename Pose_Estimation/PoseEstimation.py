import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.PoseDetector()
while True:
    success, img = cap.read()
    img = detector.find_pose(img, draw=True)
    lm_list = detector.find_position(img, draw=True)
    print(lm_list)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, f"FPS: {int(fps)}", (70,50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
