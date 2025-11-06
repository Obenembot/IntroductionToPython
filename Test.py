"""
alert_check.py (Python 3.13 compatible)
Prototype: Drowsiness + reaction-time + voice feature collector.
Not a medical device. For research/experimentation only.
"""

import time
import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
import librosa
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import random
import csv

# ---------------------------
# Part 1: Drowsiness via Eye Blink Detection (OpenCV)
# ---------------------------

# Load pre-trained Haar cascades for face and eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

def run_drowsiness_detector(blink_limit=15):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    blink_counter = 0
    frame_counter = 0
    eye_closed_frames = 0

    print("Starting drowsiness detector (press 'q' to quit).")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        eyes_detected = False
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) > 0:
                eyes_detected = True
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        if not eyes_detected:
            eye_closed_frames += 1
        else:
            if eye_closed_frames > 1:
                blink_counter += 1
            eye_closed_frames = 0

        frame_counter += 1

        cv2.putText(frame, f"Blink Count: {blink_counter}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

        if blink_counter > blink_limit:
            cv2.putText(frame, "DROWSINESS ALERT!", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

        cv2.imshow("Drowsiness Detector (press q to quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# ---------------------------
# Part 2: Reaction-time test
# ---------------------------
def reaction_time_test(trials=5):
    print("\nReaction time test:")
    print("When you see 'GO!' press ENTER as quickly as possible.")
    times = []
    for i in range(trials):
        wait = random.uniform(1.5, 4.0)
        print(f"\nTrial {i + 1}/{trials}. Get ready...")
        time.sleep(wait)
        print("GO!")
        start = time.time()
        input()  # user presses Enter
        rt = time.time() - start
        times.append(rt)
        print(f"Reaction: {rt * 1000:.0f} ms")
    avg_rt = sum(times) / len(times)
    print(f"\nAverage reaction time: {avg_rt * 1000:.0f} ms")
    return times


# ---------------------------
# Part 3: Audio capture + MFCC extraction
# ---------------------------
def record_audio(filename="sample.wav", duration=3, fs=22050):
    print(f"\nRecording {duration}s audio... speak for the sample.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    sf.write(filename, audio, fs)
    print(f"Saved {filename}")
    return filename


def extract_audio_features(filename, sr=22050, n_mfcc=13):
    y, _ = librosa.load(filename, sr=sr, mono=True)
    mfcc = librosa.feature.mfcc(y, sr=sr, n_mfcc=n_mfcc)
    zcr = librosa.feature.zero_crossing_rate(y)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    feats = {
        "mfcc_mean": np.mean(mfcc, axis=1),
        "mfcc_std": np.std(mfcc, axis=1),
        "zcr_mean": np.mean(zcr),
        "tempo": tempo,
    }
    feature_vector = np.hstack([feats["mfcc_mean"], feats["mfcc_std"], feats["zcr_mean"], feats["tempo"]])
    return feature_vector


# ---------------------------
# Part 4: Simple dataset collection & toy classifier
# ---------------------------
DATA_DIR = "collected_data"
os.makedirs(DATA_DIR, exist_ok=True)

def collect_sample(label, prefix="sample"):
    fname = f"{prefix}_{int(time.time())}.wav"
    path = os.path.join(DATA_DIR, fname)
    record_audio(path, duration=3)
    feat = extract_audio_features(path)
    return feat, label

def train_toy_classifier(X, y):
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print("\nClassification report (toy):")
    print(classification_report(y_test, preds))
    return clf


# ---------------------------
# Part 5: Main interactive menu
# ---------------------------
def main_menu():
    print("=== Alert Check Prototype ===")
    while True:
        print("\nChoose an action:")
        print("1) Run drowsiness detector (webcam)")
        print("2) Run reaction-time test")
        print("3) Record audio sample & extract features (for ML)")
        print("4) Collect labeled audio sample (for dataset)")
        print("5) Train toy classifier on collected audio (if you have dataset)")
        print("q) Quit")

        cmd = input("Choice: ").strip().lower()
        if cmd == "1":
            run_drowsiness_detector()
        elif cmd == "2":
            reaction_time_test()
        elif cmd == "3":
            f = record_audio("temp_sample.wav", duration=3)
            fv = extract_audio_features(f)
            print("Feature vector length:", len(fv))
            print(fv)
        elif cmd == "4":
            lab = input("Label this sample (0 = sober/rested, 1 = intoxicated/tired): ").strip()
            try:
                lab_i = int(lab)
                feat, label = collect_sample(lab_i, prefix="sample")
                csv_file = os.path.join(DATA_DIR, "features.csv")
                with open(csv_file, "a", newline="") as fh:
                    writer = csv.writer(fh)
                    writer.writerow(np.hstack([feat, label]))
                print("Saved features to", csv_file)
            except:
                print("Invalid label")
        elif cmd == "5":
            csv_file = os.path.join(DATA_DIR, "features.csv")
            if not os.path.exists(csv_file):
                print("No dataset found. Collect samples first (option 4).")
                continue
            X, y = [], []
            with open(csv_file, "r") as fh:
                reader = csv.reader(fh)
                for r in reader:
                    arr = np.array(r, dtype=float)
                    X.append(arr[:-1])
                    y.append(int(arr[-1]))
            train_toy_classifier(X, y)
        elif cmd == "q":
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main_menu()
