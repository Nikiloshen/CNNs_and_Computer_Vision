import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

brush_thickness = 30
eraser_thickness = 50


folder_path = "Hand_Detection/Header"
my_list = os.listdir(folder_path)

overlay_list = []
for image_path in my_list:
    image = cv2.imread(f"{folder_path}/{image_path}")
    overlay_list.append(image)

header = overlay_list[0]
draw_color = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detection_confidence=0.85)
xp, yp = 0, 0
img_canvas = np.zeros((480, 640,3), np.uint8)
while True:

    # Import Image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Find Hand Landmarks
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)

    if len(lm_list) != 0:
        # Tip of index and middle fingers
        x1, y1 = lm_list[8][1:] # Index finger
        x2, y2 = lm_list[12][1:] # Middle finger

        # Check which fingers are up
        fingers = detector.fingers_up()
        
        # If Selection Mode - Two Fingers are Up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            # Checking for the click
            if y1 < 83:
                if 125<x1<225:
                    header = overlay_list[0]
                    draw_color = (255,0,255)
                elif 275<x1<375:
                    header = overlay_list[1]
                    draw_color = (255,0,0)
                elif 400<x1<475:
                    header = overlay_list[2]
                    draw_color = (0,255,0)
                elif 525<x1<600:
                    header = overlay_list[3]
                    draw_color = (0,0,0)
            cv2.rectangle(img, (x1,y1-20), (x2,y2+20), draw_color, -1)

        # If Drawing Mode - Index Finger is Up
        if fingers[1] and not fingers[2]:
            cv2.circle(img, (x1,y1), 5, draw_color, -1)
            print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if draw_color == (0,0,0):
                cv2.line(img, (xp, yp), (x1,y1), draw_color, thickness=eraser_thickness)
                cv2.line(img_canvas, (xp, yp), (x1,y1), draw_color, thickness=eraser_thickness)
            else:
                cv2.line(img, (xp, yp), (x1,y1), draw_color, thickness=brush_thickness)
                cv2.line(img_canvas, (xp, yp), (x1,y1), draw_color, thickness=brush_thickness)

            xp, yp = x1, y1

    img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
    _, img_inverse = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inverse = cv2.cvtColor(img_inverse, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inverse)
    img = cv2.bitwise_or(img, img_canvas)


    # Setting the header image
    img[0:61, 0:640] = header
    cv2.imshow("Image", img)
    cv2.waitKey(1)