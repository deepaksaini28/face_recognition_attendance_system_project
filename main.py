import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from threading import Thread


recognition_running = False


def mark_attendance(name):
    try:
        with open('attendance.csv', 'a+') as file:
            file.seek(0)
            all_lines = file.readlines()
            name_list = [line.split(',')[0] for line in all_lines]

          
            if name not in name_list:
                now = datetime.now()
                dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
                file.write(f'{name},{dt_string}\n')
                print(f"Attendance marked for {name} at {dt_string}")
    except Exception as e:
        print(f"Error marking attendance: {e}")


def submit_attendance():
    try:
        with open('attendance.csv', 'r') as file:
            content = file.read()
            if content.strip():
                messagebox.showinfo("Attendance Submitted", "Attendance has been successfully submitted.")
            else:
                messagebox.showwarning("No Attendance", "No attendance data to submit.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Attendance file not found.")


def start_recognition():
    global recognition_running
    recognition_running = True


    path = 'Images'
    images = []
    class_names = []

    try:
        image_list = os.listdir(path)
        for image_name in image_list:
            img = cv2.imread(f'{path}/{image_name}')
            if img is not None:
                images.append(img)
                class_names.append(os.path.splitext(image_name)[0])
    except FileNotFoundError:
        messagebox.showerror("Error", "Images folder not found.")
        return

    
    encode_list = []
    for img in images:
        try:
            encode = face_recognition.face_encodings(img)[0]
            encode_list.append(encode)
        except IndexError:
            print("No face found in one of the images, skipping...")

    cap = cv2.VideoCapture(0)

    while recognition_running:
        success, frame = cap.read()
        if not success:
            print("Failed to read from webcam.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


        faces_in_frame = face_recognition.face_locations(small_frame)
        encodes_in_frame = face_recognition.face_encodings(small_frame, faces_in_frame)

        for encode_face, face_loc in zip(encodes_in_frame, faces_in_frame):
            matches = face_recognition.compare_faces(encode_list, encode_face)
            face_distances = face_recognition.face_distance(encode_list, encode_face)
            match_index = np.argmin(face_distances)

            if matches[match_index]:
                name = class_names[match_index].upper()
                mark_attendance(name)

                y1, x2, y2, x1 = face_loc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow('Attendance System', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def stop_recognition():
    global recognition_running
    recognition_running = False


def start_thread():
    thread = Thread(target=start_recognition)
    thread.start()


app = tk.Tk()
app.title("Facial Recognition Attendance System")
app.geometry("300x250")

start_button = tk.Button(app, text="Start Recognition", command=start_thread)
start_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop Recognition", command=stop_recognition)
stop_button.pack(pady=10)

submit_button = tk.Button(app, text="Submit Attendance", command=submit_attendance)
submit_button.pack(pady=10)

exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.pack(pady=10)

app.mainloop()
