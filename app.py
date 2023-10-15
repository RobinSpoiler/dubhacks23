import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route("/derek")
def login():
    return render_template("/derek.html")

<<<<<<< HEAD
@app.route("/feed")
def derek():
    return render_template("/feed.html")
=======
@app.route("/markers.js")
def markers():
    return redirect("derek.html")
>>>>>>> backend/apiintegration

