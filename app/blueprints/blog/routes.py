from app import app
from flask import render_template

@app.route('/blog')
def contact():
    return render_template('blog.html')