from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

# Scehma CREATE TABLE meeting(name TINYTEXT, description MEDIUMTEXT, picture int, Location TINYTEXT, time TINYTEXT);
# One row of data in the db {'Beer with the boies', 'We are gonna get drunk and have fun', '1', 'Andralong', '2023-05-12 18:00'}

@app.route("/")
def home():
    return "Test"

@app.route("/meeting", methods = ["Get", "Post"])
def meeting():
    if request.method == "GET": 
        cur = sqlite3.connect("meetings.db").cursor()
        try:
            data = cur.execute("SELECT * FROM meeting")
            return jsonify(data.fetchall())
        except:
            return "Server side error", 501
        
    if request.method == "POST":
        return