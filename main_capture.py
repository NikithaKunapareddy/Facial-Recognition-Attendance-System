import cv2
import pickle
import numpy as np
import os



video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Could not open webcam at index 0. Check your camera or permissions.")
    exit()

facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
if facedetect.empty():
    print("Error: Haar Cascade file not loaded properly. Please check the file path and content.")
    exit()

faces_data = []
i = 0
name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to read frame from webcam.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    print(f"Detected {len(faces)} face(s) in frame.")
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i += 1
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    print(f"Key pressed: {k}")
    # Allow 'e', 'E', 'q', 'Q', and Esc key to end
    if k in [ord('e'), ord('E'), ord('q'), ord('Q'), 27] or len(faces_data) == 100:
        print("Exiting capture loop.")
        break

video.release()
cv2.destroyAllWindows()


if len(faces_data) == 0:
    print("No faces were captured. Please try again and make sure your face is visible to the camera.")
    exit()
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(len(faces_data), -1)


if 'names.pkl' not in os.listdir('data/'):
    names = [name] * len(faces_data)
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * len(faces_data)
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)


if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)
