
# 🧑‍🏫 Teacher Portal – Student Marks Management System

A simple Flask-based web application that allows teachers to **add**, **edit**, and **delete** student marks by subject.

---

## 📌 Features

- ✅ Secure login with hashed passwords  
- 🔐 Forgot password functionality with OTP sent via email  
- ➕ Add students with subject and marks  
- ✏️ Update student records inline  
- 🗑️ Delete students  
- 📊 Auto-generated serial numbers for student list  
- ⚠️ Marks validation (0–100) and name input restrictions  
- 📧 Email via Flask-Mail (Gmail app password)  
- 🔐 OTP expires in 5 minutes for security  
- 📋 Unit, integration, and end-to-end Selenium tests  

---

## 🛠️ Technologies Used

- Python (Flask)  
- SQLite  
- Flask-Mail  
- Selenium (for E2E testing)  
- Bootstrap 5  
- Gunicorn (for deployment)  
- Render (for hosting)  
- GitHub (for version control)  

---

## 🚀 Getting Started

### 1. Clone the Project

bash
- git clone https://github.com/your-username/teacher-portal.git
- cd teacher-portal


### 2. Create a Virtual Environment
- python -m venv venv
- venv\Scripts\activate  # On Windows

### 3. Install Requirements
- pip install -r requirements.txt

### 4. Setup Environment Variables
Create a .env file based on .env.example:
- MAIL_USERNAME=your_email@gmail.com
- MAIL_PASSWORD=your_app_password  # App-specific password from Gmail
- SECRET_KEY=your_random_secret_key


### 🧪 Run the Application Locally
bash
- python app.py
Visit: http://localhost:5000

🗃️ The database (database.db) is auto-created on first run.

#### Default login:

Username: Admin

Password: Admin@Password12


### ☁️ Hosting on Render

#### 1. Push to GitHub
bash
- git init
- git remote add origin https://github.com/AsifScripts/Teacher_Student_Portal
- git add .
- git commit -m "Initial commit"
- git push -u origin main

#### 2. Deploy to Render

##### Hosted Project :- https://teacher-student-portal.onrender.com

Visit https://render.com

- Click New Web Service → Connect your GitHub repo

Configure:

- Build Command: pip install -r requirements.txt

- Start Command: gunicorn app:app

- Environment: Python

- Add Environment Variables:

- MAIL_USERNAME

- MAIL_PASSWORD

- SECRET_KEY

- Render will build and deploy your app automatically.
