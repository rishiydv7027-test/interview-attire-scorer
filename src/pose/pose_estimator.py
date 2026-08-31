"""
Step 3: MediaPipe Pose Integration
------------------------------------
Purpose: Take the person-crop from YOLOv8 and pass it to MediaPipe
to get body landmarks (shoulder, hip, knee, ankle).
These landmarks are then used to create region-crops: face, torso, feet.

TODO:
- Load MediaPipe Pose solution
- Run on cropped person image
- Extract landmark coordinates
- Use landmarks to crop face / torso / feet regions
"""

def get_landmarks(person_crop):
    """Return body landmarks for a cropped person image. Placeholder."""
    pass


def crop_regions(frame, landmarks):
    """Use landmarks to crop face, torso, feet regions. Placeholder."""
    pass
