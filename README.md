# 🛡️ AI-Powered Fake Login Page Detector (Phishing Hunter)

A Python-based web tool built with Flask that detects fake/phishing login pages using:
- Visual analysis (CNN simulation)
- OCR keyword detection
- Domain pattern analysis

---

## 🚀 Features

✅ Upload screenshot of suspected phishing page  
✅ Detects suspicious words using OCR (via pytesseract)  
✅ Simulated deep learning prediction  
✅ Checks filename for phishing domain patterns  
✅ Simple web-based UI

---

## 🧰 Requirements

- Python 3.7–3.12
- pip
- Tesseract OCR

---

## 🖥️ Tesseract Installation

### Windows:
1. Download from: https://github.com/tesseract-ocr/tesseract
2. Install and add this to your system PATH:
   ```
   C:\Program Files\Tesseract-OCR
   ```

---

## 🔧 Setup Instructions

### 1. Clone or Download this repo

Unzip or navigate into:

```bash
cd phishing-hunter
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR: source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python app.py
```

Visit:
```
http://127.0.0.1:5000/
```

---

## 🧪 Usage

- Upload a screenshot of a suspected fake login page.
- The app will:
  - Simulate a CNN-based prediction
  - Use OCR to find phishing keywords
  - Check filename for phishing domain patterns

---

## 📁 Folder Structure

```
phishing-hunter/
│
├── app.py                → Flask app entry point
├── requirements.txt      → Required dependencies
├── README.md             → You're reading it!
│
├── detector/             → Detection modules
│   ├── model.py
│   ├── ocr_analysis.py
│   └── utils.py
│
├── templates/
│   └── index.html        → Web interface
│
└── uploads/              → Temporary uploaded images
```

---

## 📌 Note

This is a proof-of-concept tool for educational use and project purposes.  
The CNN model is simulated — you can integrate a trained model easily in model.py.

---

## 🧠 Future Ideas

- Integrate real CNN model (Keras/TensorFlow)
- Store scan history
- Add login and user tracking
- Deploy on cloud (Render, Heroku, etc.)

---
Youtube link
https://youtu.be/QJ6JkNgyuYY

## 📜 License

Free to use for educational and non-commercial use.
