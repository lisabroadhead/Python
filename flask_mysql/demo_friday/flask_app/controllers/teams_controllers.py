from flask_app import app
from flask import render_template,redirect,request,session,flash
# from burger import Burger

# === Remeber to add from 
# flask_app.controllers_name import file_name 
# === to server.py  #

@app.route('/')
def index():
    return render_template('index.html')