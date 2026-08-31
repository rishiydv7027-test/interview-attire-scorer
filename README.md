# Interview Attire & Grooming Scoring System

Real-time CV dashboard that scores professional attire/grooming
(shirt-tuck, beard, hair, shoes, pants) via webcam.

## Tech Stack
- Python (AI/ML/CV)
- YOLOv8 — person detection
- MediaPipe — body landmarks
- MobileNetV2 — custom attribute classifiers
- OpenCV — webcam/image handling
- Streamlit/PyQt — dashboard

## Folder Structure
```
interview-attire-scorer/
├── src/
│   ├── detection/       # Step 2 - YOLOv8 person detection
│   ├── pose/            # Step 3 - MediaPipe landmarks
│   ├── classifiers/     # Step 5 - MobileNetV2 training + inference
│   ├── pipeline/        # Step 6 - full pipeline integration
│   ├── scoring/         # Step 7 - weighted scoring logic
│   ├── dashboard/        # Step 8 - Streamlit/PyQt dashboard (built last)
│   └── utils/           # shared helpers (FPS counter, etc.)
├── data/
│   ├── raw/              # unlabeled collected images (Step 4)
│   └── labeled/          # manually tagged images (Step 4)
├── models/               # trained MobileNetV2 weights (Step 5)
├── notebooks/            # optional Jupyter experiments
├── tests/                # test files (Step 9)
├── docs/                 # extra documentation
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Progress Log

### ✅ Step 1: Environment & Repo Setup
- Created project folder structure (see above).
- Each member sets up their own Python virtual environment:
  ```
  python -m venv venv
  venv\Scripts\activate      (Windows)
  pip install -r requirements.txt
  ```
- Shared repo: push this folder to GitHub, everyone clones and works from there.

**Errors encountered:**
- On Windows, `venv\Scripts\activate` may fail with:
  ```
  cannot be loaded because running scripts is disabled on this system
  ```
  **Fix:** run once in terminal:
  ```
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```
  then retry activation. `(venv)` should appear at the start of the terminal line once active.

### ⬜ Step 2: Webcam + YOLOv8 Person Detection
_Not started yet._

### ⬜ Step 3: MediaPipe Pose Integration
_Not started yet._

### ⬜ Step 4: Dataset Collection & Labeling
_Not started yet. (Start early — takes the most time, run in parallel with Steps 1-3.)_

### ⬜ Step 5: MobileNetV2 Classifiers
_Not started yet._

### ⬜ Step 6: Pipeline Integration
_Not started yet._

### ⬜ Step 7: Scoring Logic
_Not started yet._

### ⬜ Step 8: Dashboard
_Not started yet. (Build last — test via terminal until then.)_

### ⬜ Step 9: Optimization & Testing
_Not started yet. (Target 15-20 FPS, test different lighting/backgrounds, handle no-person/partial-body edge cases.)_

---

## New Words / Glossary
- **CV (Computer Vision):** AI field for computers to "understand" images/video.
- **OpenCV:** Library to capture/process/display images/video (not an AI model, a toolkit).
- **YOLOv8:** Pretrained model that detects objects (like "person") and draws bounding boxes.
- **MediaPipe:** Pretrained model that detects body key points (shoulder, hip, knee).
- **MobileNetV2:** Lightweight model we train ourselves to classify things (tucked/untucked, etc.).
- **Classifier:** Small AI model that decides which category an image belongs to.
- **Git/GitHub:** Tool for sharing/tracking code across the team.
- **Virtual Environment:** Isolated "box" holding only this project's packages.
- **FPS:** Frames processed per second — measure of real-time speed.
