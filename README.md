# 🧑‍🏫 Teacher Portal – Student Marks Management System

A simple Flask-based web application that allows teachers to **add**, **edit**, and **delete** student marks by subject.

---

## 🌐 Live Demo

🔗 **URL:** [https://teacher-student-portal.onrender.com](https://teacher-student-portal.onrender.com)

🧪 **Test Credentials:**
- Username :- Admin 
- Password :- Admin@Password12


---

## 📸 Screenshots

> 📍 Add screenshots here (login, dashboard, OTP email, etc.)

### Login Page
<img width="1422" height="632" alt="Teacher Login" src="https://github.com/user-attachments/assets/e1df13f9-ac7a-4f6e-ae1c-f540cd6fe042" />
<img width="891" height="377" alt="image" src="https://github.com/user-attachments/assets/f56d5518-289e-467c-84b6-a63c89a0f1ab" />

### Login :- Using Wrong Credentials
<img width="801" height="441" alt="image" src="https://github.com/user-attachments/assets/0731dcdd-61a2-41fb-a1a3-d5679491e060" />

### Forgot/Reset Password
<img width="1317" height="505" alt="Forgot Password" src="https://github.com/user-attachments/assets/cde251af-ea77-4237-ab86-9393be68146f" />

### Forgot Password - Wrong Email Address entered
<img width="1164" height="401" alt="image" src="https://github.com/user-attachments/assets/eddd73b2-aea2-4c0a-88e3-e8b209d06f13" />

### Forgot Password - OTP received on Email
<img width="776" height="406" alt="image" src="https://github.com/user-attachments/assets/4f32616a-b6af-4cfe-9110-4d3cb21ad0c2" />

### Dashboard - No Record
<img width="1582" height="482" alt="DashBoard - No record" src="https://github.com/user-attachments/assets/e45f7ecb-4737-4ae3-a31a-a6c0ca932af3" />

### Dashboard - Adding Record
<img width="1572" height="645" alt="DashBoard - Add Student record" src="https://github.com/user-attachments/assets/51644f10-24f8-4fef-86dd-cdef1d1ddea4" />
<img width="1664" height="593" alt="DashBoard - Adding Record" src="https://github.com/user-attachments/assets/ca379ea7-3f3e-46e7-ab83-5bf3ee857e3a" />

### Dashboard :- Checks for Adding name (only characters and spaces Allowed)
<img width="1513" height="640" alt="image" src="https://github.com/user-attachments/assets/19980bc9-b52d-48a7-9ab5-06c959812a5b" />

### Dashboard :- Checks for Marks name (only integer from 0 to 100 Allowed)
<img width="1382" height="491" alt="image" src="https://github.com/user-attachments/assets/025bcefc-6306-4a46-b95c-499fb5191851" />

### Dashboard :- Inline Update Record
<img width="1581" height="611" alt="Dashboard - update record" src="https://github.com/user-attachments/assets/5c58b355-e4da-4e44-9276-d4f7f69f4447" />

### Dashboard :- Record Updated Successfully
<img width="1576" height="695" alt="image" src="https://github.com/user-attachments/assets/4fa44479-02a9-4d57-8c34-4d1cdd3792c5" />

### Dashboard - With Record
<img width="1672" height="580" alt="DashBoard - with Record" src="https://github.com/user-attachments/assets/49f66ed8-ed96-42e8-8a07-1244680b93a2" />



## 📌 Features

- ✅ Secure login (hashed passwords)
- 🔐 Forgot password with OTP (via email)
- ➕ Add students by name, subject & marks
- ✏️ Edit student records inline
- 🗑️ Delete students
- 📊 Auto-increment serial numbers
- ⚠️ Marks validation (0–100), name field constraints
- 📧 Email support using Flask-Mail & Gmail App Password
- 🕐 OTP expires in 5 minutes
- ✅ Unit, integration, and end-to-end (Selenium) tests

---

## 🛠️ Built With

- Python 3.10+
- Flask
- SQLite
- Flask-Mail
- Bootstrap 5
- Selenium (for UI tests)
- Gunicorn
- Render (hosting)

---

## 🚀 Getting Started

Follow these steps to run this project locally:

### 1. Clone the Repository


git clone https://github.com/AsifScripts/Teacher_Student_Portal.git
cd Teacher_Student_Portal



### 🧪 2. (Optional) Enable Local Testing


Uncomment the following lines at the bottom of app.py if you're running the app locally:


if __name__ == '__main__':

    app.run(debug=True)  # For local testing only


### 3. Create Virtual Environment

- python -m venv venv
- venv\Scripts\activate  # For Windows


### 4. Install Dependencies
- pip install -r requirements.txt

### 5. Setup Environment Variables
Create a .env file based on .env.example:

- MAIL_USERNAME=your_email@gmail.com
- MAIL_PASSWORD=your_gmail_app_password
- SECRET_KEY=your_secret_key


### 6. Run the App
- python app.py
🔗 Visit: http://localhost:5000

📦 A database.db file will be auto-created on first run.


### ☁️ Hosting on Render
Push this code to GitHub

Create a new Web Service on https://render.com

Set these options:

- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
- Runtime: Python
Add environment variables:

- MAIL_USERNAME
- MAIL_PASSWORD
- SECRET_KEY

✅ That’s it — Render will build and deploy your Flask app.

### 👨‍💻 Author
Asif – https://github.com/AsifScripts

### 📄 License
This project is open-source and available under the MIT License.
