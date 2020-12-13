import os
import urllib
import webbrowser
from flask import Flask,current_app as app, render_template, request



@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/universitiesdetails')
def universitydetails():
    return render_template("university-details.html")

@app.route('/universities')
def universities():
    return render_template("universities.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/administrators')
def administrators():
    return render_template("administrators.html")