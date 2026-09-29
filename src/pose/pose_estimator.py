"""
Step 3: MediaPipe Pose Integration
------------------------------------
Purpose: Take the person-crop from YOLOv8 and pass it to MediaPipe
to get body landmarks (shoulder, hip, knee, ankle).
These landmarks are then used to create region-crops: face, torso, feet.
"""
import mediapipe as mp #Google Pretrained model to detect 33 body Points [assigns coordinates]
import cv2 #Takes frame from Camera 

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)


def get_landmarks(person_crop):
    """Return body landmarks for a cropped person image."""
    rgb_crop = cv2.cvtColor(person_crop, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_crop)
    if results.pose_landmarks is None:
        return None
    return results.pose_landmarks.landmark


def crop_regions(frame, landmarks):
    """Use landmarks to crop face, torso, feet regions."""
    h, w, _ = frame.shape

    def to_pixel(landmark):
        return int(landmark.x * w), int(landmark.y * h)

    nose_x, nose_y = to_pixel(landmarks[0])
    l_shoulder = to_pixel(landmarks[11])
    r_shoulder = to_pixel(landmarks[12])
    l_hip = to_pixel(landmarks[23])
    r_hip = to_pixel(landmarks[24])
    l_ankle = to_pixel(landmarks[27])
    r_ankle = to_pixel(landmarks[28])

    # Face region: nose ke around box
    face_size = 80
    face_crop = frame[max(0, nose_y - face_size): nose_y + face_size,
                       max(0, nose_x - face_size): nose_x + face_size]

    # Torso region: shoulder se hip tak (shirt-tuck ke liye)
    torso_top = min(l_shoulder[1], r_shoulder[1])
    torso_bottom = max(l_hip[1], r_hip[1])
    torso_left = min(l_shoulder[0], r_shoulder[0], l_hip[0], r_hip[0])
    torso_right = max(l_shoulder[0], r_shoulder[0], l_hip[0], r_hip[0])
    torso_crop = frame[torso_top:torso_bottom, torso_left:torso_right]

    # Feet region: ankle ke around, frame ke bottom tak
    feet_top = min(l_ankle[1], r_ankle[1]) - 30
    feet_crop = frame[max(0, feet_top):h, 0:w]

    return {
        "face": face_crop,
        "torso": torso_crop,
        "feet": feet_crop
    }