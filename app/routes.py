from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
