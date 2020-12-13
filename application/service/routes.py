import os
import urllib
import webbrowser
from flask import Flask,current_app as app, render_template, request



@app.route('/', methods=["GET"])
def hello_world():
    return render_template("index.html")

@app.route('/index', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route('/universitiesdetails', methods=["GET"])
def universitydetails():
    return render_template("university-details.html")

@app.route('/universities', methods=["GET"])
def universities():
    return render_template("universities.html")

@app.route('/events', methods=["GET"])
def events():
    return render_template("events.html")

@app.route('/administrators', methods=["GET"])
def administrators():
    return render_template("administrators.html")