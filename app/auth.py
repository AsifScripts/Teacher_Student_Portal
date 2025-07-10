from flask import Blueprint, render_template, request, redirect, session, flash
import hashlib
from init__db import get_db_connection

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = hashlib.sha256(request.form['password'].encode()).hexdigest()

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM teachers WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()

    if user:
        session['user'] = username
        return redirect('/dashboard')
    else:
        flash('Invalid credentials')
        return redirect('/')
