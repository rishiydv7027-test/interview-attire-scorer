"""
Step 3: MediaPipe Pose Integration
------------------------------------
Purpose: Take the person-crop from YOLOv8 and pass it to MediaPipe
to get body landmarks (shoulder, hip, knee, ankle).
These landmarks are then used to create region-crops: face, torso, feet.
"""
import mediapipe as mp
import cv2

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
    """Use landmarks to crop face, torso, feet regions. Placeholder."""
    pass