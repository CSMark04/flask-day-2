from app import app
from flask import render_template

@app.route('/login')
def contact():
    return render_template('login.html')

@app.route('/register')
def contact():
    return render_template('regoster.html')

