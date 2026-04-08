import tkinter as tk
from tkinter import *
import os, cv2
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "TrainingImageLabel\\Trainner.yml"
trainimage_path = "TrainingImage"
studentdetail_path = "StudentDetails\\studentdetails.csv"
attendance_path = "Attendance"


def subjectChoose(text_to_speech):

    def FillAttendance():
        sub = tx.get()

        if sub == "":
            text_to_speech("Please enter the subject name!!!")
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()

            try:
                recognizer.read(trainimagelabel_path)
            except:
                msg = "Model not found, please train model"
                Notifica.config(text=msg)
                text_to_speech(msg)
                return

            faceCascade = cv2.CascadeClassifier(haarcasecade_path)
            df = pd.read_csv(studentdetail_path)
            cam = cv2.VideoCapture(0)

            col_names = ["Enrollment", "Name"]
            attendance = pd.DataFrame(columns=col_names)

            start_time = time.time()
            end_time = start_time + 20

            while True:
                ret, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.2, 5)

                for x, y, w, h in faces:
                    Id, conf = recognizer.predict(gray[y : y + h, x : x + w])

                    if conf < 70:
                        name = str(df.loc[df["Enrollment"] == Id]["Name"].values[0])
                        label = f"{Id}-{name}"

                        attendance.loc[len(attendance)] = [Id, name]

                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(
                            im,
                            label,
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (255, 255, 0),
                            2,
                        )

                cv2.imshow("Filling Attendance...", im)

                if time.time() > end_time:
                    break

                if cv2.waitKey(1) == 27:
                    break

            cam.release()
            cv2.destroyAllWindows()

            # Save attendance
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            timeStamp = datetime.datetime.now().strftime("%H-%M-%S")

            attendance[date] = 1
            attendance.drop_duplicates(["Enrollment"], keep="first", inplace=True)

            folder = os.path.join(attendance_path, sub)
            os.makedirs(folder, exist_ok=True)

            fileName = os.path.join(folder, f"{sub}_{date}_{timeStamp}.csv")
            attendance.to_csv(fileName, index=False)

            msg = f"Attendance Filled Successfully for {sub}"
            Notifica.config(text=msg)
            text_to_speech(msg)

            # Display CSV
            root = tk.Tk()
            root.title(f"Attendance of {sub}")
            root.configure(bg="black")

            with open(fileName) as file:
                reader = csv.reader(file)

                for r, row in enumerate(reader):
                    for c, val in enumerate(row):
                        tk.Label(
                            root, text=val, width=12, bg="black", fg="yellow"
                        ).grid(row=r, column=c)

            root.mainloop()

        except:
            text_to_speech("No Face found for attendance")

    def Attf():
        sub = tx.get()

        if sub == "":
            text_to_speech("Please enter the subject name!!!")
        else:
            folder = os.path.join("Attendance", sub)

            if os.path.exists(folder):
                os.startfile(folder)
            else:
                text_to_speech("No attendance found")

    # GUI
    subject = tk.Tk()
    subject.title("Subject")
    subject.geometry("580x320")
    subject.configure(bg="black")

    tk.Label(
        subject, text="Enter Subject Name", bg="black", fg="green", font=("Arial", 25)
    ).place(x=140, y=20)

    Notifica = tk.Label(subject, text="", bg="yellow", fg="black", width=33, height=2)
    Notifica.place(x=20, y=250)

    tk.Label(
        subject, text="Subject", bg="black", fg="yellow", font=("Arial", 15)
    ).place(x=50, y=100)

    tx = tk.Entry(subject, font=("Arial", 20))
    tx.place(x=200, y=100)

    tk.Button(subject, text="Fill Attendance", command=FillAttendance).place(
        x=200, y=180
    )

    tk.Button(subject, text="Check Sheets", command=Attf).place(x=350, y=180)

    subject.mainloop()
