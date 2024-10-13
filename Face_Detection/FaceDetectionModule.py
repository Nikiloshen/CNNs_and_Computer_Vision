import cv2
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, min_detection_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.min_detection_confidence)

    def find_faces(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        bboxes = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                # mpDraw.draw_detection(img, detection)
                # print(detection.location_data.relative_bounding_box)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                bboxes.append([id, bbox, detection.score])
                img = self.fancy_draw(img, bbox)
                cv2.putText(img, f"{int(detection.score[0]*100)}%", (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 2)

        return img, bboxes
    
    def fancy_draw(self, img, bbox, length=30, thickness=5):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, (255,0,255), 1)
        # Top left x, y
        cv2.line(img, (x,y), (x+length, y), (255,0,255), thickness)
        cv2.line(img, (x,y), (x, y+length), (255,0,255), thickness)
        # Top right, x1, y
        cv2.line(img, (x1,y), (x1-length, y), (255,0,255), thickness)
        cv2.line(img, (x1,y), (x1, y+length), (255,0,255), thickness)
        # Bottom left x, y1
        cv2.line(img, (x,y1), (x+length, y1), (255,0,255), thickness)
        cv2.line(img, (x,y1), (x, y1-length), (255,0,255), thickness)
        # Bottom right, x1, y1
        cv2.line(img, (x1,y1), (x1-length, y1), (255,0,255), thickness)
        cv2.line(img, (x1,y1), (x1, y1-length), (255,0,255), thickness)
        return img


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0

    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxes = detector.find_faces(img, draw=True)
        print(bboxes)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img, f"FPS: {int(fps)}", (20,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()