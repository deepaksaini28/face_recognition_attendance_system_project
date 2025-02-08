# face_recognition_system_project


#Overview

This project is a facial recognition-based attendance system using OpenCV and face_recognition libraries in Python. It captures faces via a webcam, matches them with pre-stored images, and marks attendance in a CSV file.

#Features

Real-time face recognition

Attendance marking with timestamps

Simple GUI using Tkinter

CSV-based attendance storage

Installation

Prerequisites

Ensure you have Python installed (Python 3.x recommended).

Install Dependencies

Run the following command to install required libraries:

pip install -r requirements.txt

Usage

Store Images: Place reference images in the Images folder. The file name (excluding extension) should be the person's name.

Run the Application:

python your_script_name.py

Start Recognition: Click Start Recognition in the GUI.

Stop Recognition: Click Stop Recognition to stop face detection.

Submit Attendance: Click Submit Attendance to finalize attendance.

Exit: Click Exit to close the application.

File Structure

Facial-Recognition-Attendance/
│-- Images/                 # Folder for storing reference images
│-- attendance.csv          # Stores marked attendance records
│-- requirements.txt        # Dependencies
│-- your_script_name.py     # Main script
│-- README.md               # Project documentation

Dependencies

opencv-python

face-recognition

numpy

tkinter (built-in with Python)

Notes

Ensure good lighting for better recognition.

Press q to quit the camera window if stuck.

Faces in the Images folder must be clear and well-lit.


Author

Deepak Saini

Version Control

This project is managed using GitHub. Follow these steps to upload your project:

Initialize Git and Push to GitHub

Initialize a git repository:

git init

Add all project files:

git add .

Commit the changes:

git commit -m "Initial commit"

Add a remote repository:

git remote add origin https://github.com/deepaksaini28/repositoryname.git

Push to GitHub:
