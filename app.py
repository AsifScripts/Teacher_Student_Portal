import os
import sqlite3
import random
import time
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from init__db import init_database
from dotenv import load_dotenv

# 🧱 Initialize the SQLite DB (safe to call repeatedly)
init_database()
load_dotenv()

# 🔧 Flask app & mail config
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Replace default in production

app.config.update({
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'MAIL_DEFAULT_SENDER': os.getenv('MAIL_USERNAME')  # Needed to avoid AssertionError
})

mail = Mail(app)
otp_store = {}  # ⏳ In-memory OTP cache

# 📁 DB connection
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ====================== ROUTES ======================

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()

    if user and check_password_hash(user['password'], password):
        session['user'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html', error='Invalid credentials')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('dashboard.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name'].strip()
    subject = request.form['subject'].strip()
    try:
        marks = int(request.form['marks'])
        if marks < 0 or marks > 100:
            raise ValueError
    except ValueError:
        return redirect(url_for('dashboard'))

    with get_db_connection() as conn:
        existing = conn.execute(
            "SELECT * FROM students WHERE name = ? AND subject = ?", (name, subject)
        ).fetchone()

        if existing:
            # Add the new marks to existing marks
            total_marks = existing['marks'] + marks
            conn.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (total_marks, existing['id'])
            )
        else:
            # Insert new record
            conn.execute(
                "INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)",
                (name, subject, marks)
            )
        conn.commit()

    return redirect(url_for('dashboard'))


@app.route('/update_student', methods=['POST'])
def update_student():
    data = request.json
    try:
        with get_db_connection() as conn:
            conn.execute("UPDATE students SET name = ?, subject = ?, marks = ? WHERE id = ?",
                         (data['name'], data['subject'], data['marks'], data['id']))
            conn.commit()
        return jsonify(status='success')
    except Exception as e:
        return jsonify(status='error', message=str(e))

@app.route('/delete_student/<int:id>')
def delete_student(id):
    try:
        with get_db_connection() as conn:
            conn.execute("DELETE FROM students WHERE id = ?", (id,))
            conn.commit()
        return redirect(url_for('dashboard'))
    except Exception as e:
        return f"Error deleting student: {e}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# =================== FORGOT PASSWORD FLOW ===================

@app.route('/forgot', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email'].strip()

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        if not user:
            return render_template('forgot_password.html', error='User not found')

        otp = str(random.randint(100000, 999999))
        otp_store[email] = {'otp': otp, 'timestamp': time.time()}

        msg = Message("Teacher Portal Password Reset OTP", recipients=[email])
        msg.body = (
            f"You're receiving this OTP because you requested a password reset for Teacher Portal.\n\n"
            f"Your OTP is: {otp}\n\n"
            f"⚠️ Do not share this with anyone.\n"
            f"This OTP will expire in 5 minutes."
        )
        mail.send(msg)

        return render_template('verify_otp.html', email=email)
    return render_template('forgot_password.html')

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    otp = request.form['otp']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    otp_entry = otp_store.get(email)

    if not otp_entry:
        return render_template('verify_otp.html', email=email, error='OTP expired or invalid. Please try again.')

    if time.time() - otp_entry['timestamp'] > 300:
        otp_store.pop(email, None)
        return render_template('verify_otp.html', email=email, error='OTP has expired. Please request a new one.')

    if otp_entry['otp'] != otp:
        return render_template('verify_otp.html', email=email, error='Invalid OTP.')

    if new_password != confirm_password:
        return render_template('verify_otp.html', email=email, error='Passwords do not match.')

    conn = get_db_connection()
    hashed_pwd = generate_password_hash(new_password)
    conn.execute("UPDATE users SET password = ? WHERE email = ?", (hashed_pwd, email))
    conn.commit()
    conn.close()

    otp_store.pop(email, None)
    return render_template('login.html', success='Password reset successful. Please log in.')

# =================== RUN ===================
# if __name__ == '__main__':
#    app.run(debug=False)  # Use debug=False in production
