"""
Step 6: Pipeline Integration
--------------------------------
Flow: Camera -> YOLOv8 (detect) -> MediaPipe (landmarks) -> crops -> classifiers -> results.

TODO:
- Import detect_person from src/detection/yolo_detector.py
- Import get_landmarks, crop_regions from src/pose/pose_estimator.py
- Import predict from src/classifiers/predict.py
- Chain everything together into one function that takes a frame
  and returns classifier results for all attributes
"""

def run_pipeline(frame):
    """Run the full detection -> pose -> classification pipeline on a frame. Placeholder."""
    pass
