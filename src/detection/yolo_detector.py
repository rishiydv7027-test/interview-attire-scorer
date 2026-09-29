"""
Step 2: Webcam + YOLOv8 Person Detection
------------------------------------------
Purpose: Capture webcam frames using OpenCV, run YOLOv8n (pretrained)
to detect "person" and draw a bounding box.
"""
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')


def detect_person(frame):
    """
    Run YOLOv8 person detection on a single frame.
    Returns: cropped person image (numpy array) or None if no person found.
    """
    results = model(frame, classes=[0], verbose=False)  # class 0 = person (COCO dataset)

    boxes = results[0].boxes
    if len(boxes) == 0:
        return None

    box = boxes[0]
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    person_crop = frame[y1:y2, x1:x2]
    return person_crop


def run_webcam_loop():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No Frame detected From Camera")
            break

        person_crop = detect_person(frame)

        if person_crop is not None:
            cv2.imshow("Person Crop", person_crop)
        else:
            print("No Person Detected")

        cv2.imshow("Webcam Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_webcam_loop()