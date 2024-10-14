import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folder_path = "Hand_Detection/FingerImages"
my_list = os.listdir(folder_path)
print(my_list)
overlay_list = []
for im_path in my_list:
    image = cv2.imread(f"{folder_path}/{im_path}")
    overlay_list.append(image)


pTime = 0

detector = htm.HandDetector()

tip_ids = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    print(lm_list)

    if len(lm_list) != 0:
        fingers = []

        # Thumb
        if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0)
            
        # 4 Fingers
        for id in range(1,5):
            if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = fingers.count(1)
        print(total_fingers)

        h,w,c = overlay_list[total_fingers-1].shape
        img[0:h, 0:w] = overlay_list[total_fingers-1]

        cv2.rectangle(img, (20,225), (170,425), (0,255,0), -1)
        cv2.putText(img, f"{total_fingers}", (45,375), cv2.FONT_HERSHEY_SIMPLEX,10,(255,0,0), 25)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)