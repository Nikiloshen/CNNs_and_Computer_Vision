import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("Pose_Estimation/AiTrainer/curls.mp4")

detector = pm.PoseDetector()
count = 0
dir = 0

pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.find_pose(img, False)
    lm_list = detector.find_position(img, False)
    if len(lm_list) != 0:
        # # Right Arm
        # detector.find_angle(img, 12, 14, 16)
        # Left Arm
        angle = detector.find_angle(img, 11, 13, 15)
        per = np.interp(angle, (210,310), (0,100))
        bar = np.interp(angle, (220,310), (650, 100))
        print(per)

        # Check for the dumbbell curls
        color = (255,0,255) 
        if per == 100:
            color = (0,255,0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0,255,0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # Draw Bar
        cv2.rectangle(img, (1100,100), (1175,650), color, 3)
        cv2.rectangle(img, (1100,int(bar)), (1175,650), color, -1)
        cv2.putText(img, f"{int(per)}%" (1100,75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0,450), (250,720), (0,255,0), -1)
        cv2.putText(img, f"{int(count)}", (45,670), cv2.FONT_HERSHEY_PLAIN, 15, (255,0,0), 25)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f"{int(fps)}", (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)