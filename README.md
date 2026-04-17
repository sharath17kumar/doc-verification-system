# 📄 AI Document Verification System

## 🚀 Overview

The **AI Document Verification System** is a backend-based application that verifies the authenticity of documents or signatures by comparing two images using computer vision techniques.

It uses image similarity logic to determine whether the uploaded documents match and provides a similarity score as output.

---

## 🧠 Features

* User Registration & Login (Authentication)
* Upload and process document images
* Compare two images for verification
* Generate similarity score
* Match / Not Match decision based on threshold
* RESTful APIs with Swagger UI support

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **AI/Logic:** OpenCV (Image Processing)
* **Authentication:** JWT (python-jose, passlib)
* **Language:** Python

---

## 📂 Project Structure

```bash
doc-verification-system/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── auth.py
│   ├── routes/
│   ├── utils/
│── venv/
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/doc-verification-system.git
cd doc-verification-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Once the server is running, open:

```bash
http://127.0.0.1:8000/docs
```

This will open Swagger UI where you can test all APIs.

---

## 📊 How It Works

1. User uploads two images
2. Images are converted to grayscale and resized
3. Image similarity is computed using computer vision techniques
4. A similarity score is generated (0 to 1)
5. If score > threshold → **Matched**
6. Else → **Not Matched**

---

## 🔥 Sample Output

```json
{
  "similarity_score": 0.87,
  "status": "Matched"
}
```

---

## 🤖 AI Logic Used

This project uses basic **Computer Vision** techniques for image comparison:

* Image preprocessing (grayscale conversion, resizing)
* Structural similarity comparison (SSIM)
* Threshold-based verification logic

---

## ☁️ Deployment

### 🚀 Current Status

The project is currently running in a local development environment using FastAPI.

---

☁️ AWS Deployment (Implemented)

This project was successfully deployed on Amazon EC2 for cloud-based testing and demonstration.

🔧 Deployment Steps

1️⃣ Launch EC2 Instance

Go to AWS Console → EC2
Launch instance (Ubuntu)
Instance type: t2.micro / t3.micro (Free Tier)
Create & download key pair (.pem)

2️⃣ Configure Security Group

Allow:
SSH (Port 22)
HTTP (Port 80)
Custom TCP (Port 8000)

3️⃣ Connect to EC2

ssh -i your-key.pem ubuntu@your-public-ip

4️⃣ Install Required Packages

sudo apt update
sudo apt install python3-pip python3-venv git -y

5️⃣ Setup Virtual Environment

python3 -m venv venv
source venv/bin/activate

6️⃣ Install Dependencies

pip install -r requirements.txt

7️⃣ Run Application

uvicorn app.main:app --host 0.0.0.0 --port 8000

8️⃣ Access Application

http://<your-ec2-public-ip>:8000/docs.

---

### 💡 Future Improvements

* Add frontend (React / HTML UI)
* Deploy application on cloud (AWS / Render)
* Integrate OCR for text extraction
* Use deep learning models for better accuracy
* Add face/signature recognition

---

## 👨‍💻 Author

Sharath Kumar R
sharathkumar2003r@gmail.com
https://www.linkedin.com/in/sharath-kumar-r06/
---
