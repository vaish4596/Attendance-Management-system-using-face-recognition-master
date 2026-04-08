Here’s a **clean, professional README.md description** for your project 👇 (you can directly paste into GitHub)

---

# 📌 **Smart Attendance System using Face Recognition**

## 📖 Description

The **Smart Attendance System using Face Recognition** is a Python-based application that automates the process of recording student attendance using computer vision techniques. The system captures facial images through a webcam, recognizes registered students, and marks attendance automatically.

It eliminates the need for manual attendance, reduces errors, and prevents proxy attendance. Attendance data is stored in CSV format and can be viewed and analyzed easily.

---

## 🚀 Features

* 👤 Student registration using webcam
* 🎥 Face detection using OpenCV
* 🧠 Face recognition using trained model
* ✅ Automatic attendance marking
* 📊 Attendance stored in CSV files
* 📈 Attendance percentage calculation
* 🖥️ Simple GUI using Tkinter

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Tkinter
* Pandas
* NumPy

---

## 📂 Project Structure

```text
Smart-Attendance-System/
│
├── Attendance/              # Stores attendance CSV files
├── StudentDetails/          # Stores student data
├── TrainingImage/           # Captured images
├── TrainingImageLabel/      # Trained model file
│
├── attendance.py            # Main UI file
├── takeImage.py             # Capture images
├── trainImage.py            # Train model
├── automaticAttedance.py    # Mark attendance
├── show_attendance.py       # View attendance
│
└── haarcascade_frontalface_default.xml
```

---

## ⚙️ How It Works

1. Register a new student (capture face images)
2. Train the model using captured images
3. Start attendance using webcam
4. System detects and recognizes faces
5. Attendance is automatically marked
6. CSV file is generated for each session
7. Attendance percentage can be viewed

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd Smart-Attendance-System
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the project

```bash
python attendance.py
```

---

## 📊 Output

* Attendance stored in `Attendance/Subject/` folder
* CSV file with:

  * Enrollment Number
  * Name
  * Date-wise attendance
* Final attendance report with percentage

---

## 📸 Screenshots

*(Add your project screenshots here for better presentation)*

---

## ✅ Advantages

* Saves time
* Reduces manual work
* Prevents proxy attendance
* Easy to use
* Accurate results

---

## ⚠️ Limitations

* Requires proper lighting
* Depends on camera quality
* Initial training required

---

## 🔮 Future Enhancements

* Web-based system using Flask
* Database integration (MySQL/Firebase)
* Mobile app support
* Deep learning-based face recognition

---

## 📚 References

* OpenCV Documentation
* Python Documentation
* Pandas Documentation

---

## 👩‍💻 Author

**Vaishnavi Shetty**
B.E – Information Science and Engineering

---


✅ Add **badges & styling (cool look)**
✅ Make it **resume-ready project**
