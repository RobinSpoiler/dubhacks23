import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/derek")
def derek():
    return render_template("/derek.html")

@app.route("/markers.js")
def markers():
    return redirect("derek.html")

