import os

from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db = sqlite3.connect("neighbor.db")



@app.route("/", methods=["GET", "POST"])
def index(): 
    return render_template("home.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "login" in request.form:
            return render_template("login.html")
        elif "signup" in request.form:
            return render_template("signup.html")
    else:
        return render_template("home.html")
# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # """Log user in"""
        
    # Forget any user_id
    

    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return render_template("apology.html")
    
    with sqlite3.connect("neighbor.db") as users:
    # with sqlite3.connect("neighbor.db") as users:
        cursor = users.cursor()
        sql = "SELECT * FROM users WHERE username = :un"
        par = {"un": request.form["username"]}
        cursor.execute(sql, par)
        rows = cursor.fetchall()
        if len(rows) != 1 or not check_password_hash(rows[0][2], password):
            return render_template("apology.html")
        

        return redirect("/feed")
    
    
@app.route("/signup", methods=["POST", "GET"])
def signup():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    # checks for repeated usernames

    if not username or not password or not confirmation:
        return render_template("apology.html")

    if confirmation != password:
        return render_template("apology.html")
    has_repeat = False
    with sqlite3.connect("neighbor.db") as users: 
        cursor = users.cursor()
        cursor.execute("SELECT username FROM users")
        
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            if row[0] == username.lower():
                hasRepeat = True
    
        if has_repeat:
            return render_template("apology.html")
        sql = "INSERT INTO users (username, hash) VALUES(:un, :pw)"
        par = {"un": username, "pw": generate_password_hash(password)}
        cursor.execute(sql, par)
        return render_template("login.html")


@app.route("/feed", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        return render_template("feed.html")
    return render_template("feed.html")

@app.route("/post", methods=["POST", "GET"])
def post():
    if request.method == "GET":
        return render_template("post.html")
    longitude = request.form.get("longitude")
    latitude = request.form.get("latitude")
    item = request.form.get("item")
    time = request.form.get("time")
    

    if not longitude or not latitude or not item or not time:
        return render_template("apology.html")
    
    # send to sql server

    with sqlite3.connect("neighbor.db") as users:
        cursor = users.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS markers ("longitude" TEXT, "latitude" TEXT, "item" TEXT, "time" TEXT);')
        
        sql = "INSERT INTO markers (longitude, latitude, item, time) VALUES (:lon, :lat, :item, :time)"
        par = {"lon": longitude, "lat": latitude, "item": item, "time": time}
        cursor.execute(sql, par)

        cursor.execute("SELECT * FROM markers")
        rows = cursor.fetchall()

        markers = []  # Your list of markers here

        for marker in rows:
            longitude = marker[0]
            latitude = marker[1]
            item = marker[2]
            time = marker[3]

            if longitude and latitude and item and time:
                markers.append({
                    'longitude': longitude,
                    'latitude': latitude,
                    'item': item,
                    'time': time
            })

        # Send the information to JavaScript
        response_data = {'markers': markers}

        # Instead of returning jsonify, you can return the JSON data
        return jsonify(response_data)
        



if __name__ == '__main__':
    app.run(port=5000)