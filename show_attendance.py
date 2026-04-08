import pandas as pd
from glob import glob
import os
import tkinter as tk
import csv


def subjectchoose(text_to_speech):

    def calculate_attendance():
        Subject = tx.get()

        if Subject == "":
            text_to_speech("Please enter the subject name.")
            return

        path = f"Attendance\\{Subject}"

        if not os.path.exists(path):
            text_to_speech("No attendance folder found")
            return

        filenames = glob(f"{path}\\{Subject}*.csv")

        if len(filenames) == 0:
            text_to_speech("No attendance files found")
            return

        df_list = [pd.read_csv(f) for f in filenames]

        newdf = df_list[0]

        for i in range(1, len(df_list)):
            newdf = newdf.merge(df_list[i], how="outer")

        newdf.fillna(0, inplace=True)

        # Calculate percentage
        attendance_cols = newdf.columns[2:]
        newdf["Attendance"] = newdf[attendance_cols].mean(axis=1) * 100
        newdf["Attendance"] = newdf["Attendance"].astype(int).astype(str) + "%"

        # Save result
        final_file = f"{path}\\attendance.csv"
        newdf.to_csv(final_file, index=False)

        # Display in GUI
        root = tk.Tk()
        root.title("Attendance of " + Subject)
        root.configure(bg="black")

        with open(final_file) as file:
            reader = csv.reader(file)

            for r, row in enumerate(reader):
                for c, val in enumerate(row):
                    tk.Label(root, text=val, width=12, fg="yellow", bg="black").grid(
                        row=r, column=c
                    )

        root.mainloop()

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
        subject, text="Which Subject?", bg="black", fg="green", font=("Arial", 25)
    ).place(x=120, y=20)

    tk.Label(
        subject, text="Enter Subject", bg="black", fg="yellow", font=("Arial", 15)
    ).place(x=50, y=100)

    tx = tk.Entry(subject, font=("Arial", 20))
    tx.place(x=200, y=100)

    tk.Button(subject, text="View Attendance", command=calculate_attendance).place(
        x=200, y=180
    )

    tk.Button(subject, text="Check Sheets", command=Attf).place(x=350, y=180)

    subject.mainloop()
