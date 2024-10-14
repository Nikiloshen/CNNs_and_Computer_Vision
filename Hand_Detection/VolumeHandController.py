import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

######################
wCam, hCam = 640, 480
######################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.HandDetector(detection_confidence=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]
vol = 0
vol_bar = 400
vol_percentage = 0


while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, False)
    if len(lm_list) != 0:
        print(lm_list[4], lm_list[8])

        x1,y1 = lm_list[4][1], lm_list[4][2]
        x2,y2 = lm_list[8][1], lm_list[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2


        cv2.circle(img, (x1,y1), 15, (255,0,255), -1)
        cv2.circle(img, (x2,y2), 15, (255,0,255), -1)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)

        length = math.hypot(x2-x1, y2-y1)

        # Hand range 50-300
        # Volume range -64-0

        vol = np.interp(length, [50,300], [min_vol, max_vol])
        vol_bar = np.interp(length, [50,300], [400,150])
        vol_percentage = np.interp(length, [50,300], [0,100])
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx,cy), 15, (0,255,0), -1)

    cv2.rectangle(img, (50,150),(85,400), (0,255,0), 3)
    cv2.rectangle(img, (50,int(vol_bar)),(85,400), (0,255,0), -1)
    cv2.putText(img, f"{int(vol_percentage)}", (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)