from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models
from .auth import hash_password, verify_password
from fastapi import UploadFile, File
import shutil
import os
import cv2

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API is running 🚀"}


# 🔐 REGISTER API
@app.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = models.User(
        email=email,
        password=hash_password(password)
    )
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}


# 🔑 LOGIN API
@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return {"error": "User not found"}

    if not verify_password(password, user.password):
        return {"error": "Invalid password"}

    return {"message": "Login successful"}

# Uploads API
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "File uploaded successfully"}

# Compare API
def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)

    if img1 is None or img2 is None:
        return "Error reading images"

    if img1.shape != img2.shape:
        return 0

    difference = cv2.absdiff(img1, img2)
    score = 100 - (difference.sum() / (img1.size * 255) * 100)

    return round(score, 2)

@app.post("/compare")
def compare(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    path1 = os.path.join(UPLOAD_DIR, file1.filename)
    path2 = os.path.join(UPLOAD_DIR, file2.filename)

    with open(path1, "wb") as f:
        shutil.copyfileobj(file1.file, f)

    with open(path2, "wb") as f:
        shutil.copyfileobj(file2.file, f)

    score = compare_images(path1, path2)

    return {
        "similarity_score": score
    }