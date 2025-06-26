# Facial Recognition Attendance System

This project is an intelligent attendance system using facial recognition with OpenCV and KNN. It captures faces via webcam, recognizes individuals, and logs attendance with timestamps in a CSV file. The system is trained on labeled images using Pickle and is ideal for eliminating proxy and manual attendance.

## Features
- Real-time face detection and recognition
- Attendance logging with timestamps
- Uses OpenCV, scikit-learn, and NumPy
- Stores attendance in CSV files

## Requirements
See `requirements.txt` for dependencies.

## Usage
1. Ensure you have the required dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your trained data files (`data/names.pkl`, `data/faces_data.pkl`, and `data/haarcascade_frontalface_default.xml`) in a `data` folder.
3. Run the main script:
   ```bash
   python recognize_and_mark_attendance.py
   ```
4. Press 'o' to mark attendance, 'q' to quit.

## Folder Structure
- `main_capture.py` - Script for capturing and training faces
- `recognize_and_mark_attendance.py` - Script for recognizing faces and marking attendance
- `background.png` - Background image for the UI
- `Attendance/` - Folder where attendance CSVs are saved
- `data/` - Folder for model and cascade files

## Author
Nikitha Kunapareddy
