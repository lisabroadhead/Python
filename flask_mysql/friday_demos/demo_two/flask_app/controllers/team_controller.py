from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.team_model import Team

# === Remeber to add from 
# flask_app.controllers_name import file_name 
# === to server.py  #

@app.route('/')
def index():
    all_teams = Team.get_all_teams()
    return render_template('index.html',all_teams = all_teams)