import cv2
import mediapipe as mp
import time
import math

class PoseDetector():
    def __init__(self, mode=False, upper_body=False, smooth=True, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.upper_body = upper_body
        self.smooth = smooth
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, 
                                     enable_segmentation=self.upper_body, 
                                     smooth_segmentation=self.smooth, 
                                     min_detection_confidence=self.detection_confidence, 
                                     min_tracking_confidence=self.track_confidence)

    def find_pose(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img
    
    def find_position(self, img, draw=True):
        self.lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lm_list.append([id, cx, cy])
                if draw:
                   cv2.circle(img, (cx, cy), 8, (255,0,0), -1)
        return self.lm_list
    
    def find_angle(self, img, p1, p2, p3, draw=True):

        # Get the landmarks
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        x3, y3 = self.lm_list[p3][1:]

        # Calculate the angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))

        if angle < 0:
            angle += 360

        # Draw
        if draw:
            cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 3)
            cv2.line(img, (x2,y2), (x3,y3), (255,255,255), 3)
            cv2.circle(img, (x1, y1), 10, (0,0,255), -1)
            cv2.circle(img, (x1, y1), 15, (0,0,255), 2)
            cv2.circle(img, (x2, y2), 10, (0,0,255), -1)
            cv2.circle(img, (x2, y2), 15, (0,0,255), 2)
            cv2.circle(img, (x3, y3), 10, (0,0,255), -1)
            cv2.circle(img, (x3, y3), 15, (0,0,255), 2)
            # cv2.putText(img, f"{int(angle)}", (x2-20, y2+50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
        
        return angle



def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = PoseDetector()
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

if __name__ == "__main__":
    main()
