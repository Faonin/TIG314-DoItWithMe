from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

cur = sqlite3.connect("meetings.db").cursor()

# Scehma CREATE TABLE meeting(name TINYTEXT, description MEDIUMTEXT, picture int, Location TINYTEXT, time TINYTEXT);
# One row of data in the db {'Beer with the boies', 'We are gonna get drunk and have fun', '1', 'Andralong', '2023-05-12 18:00'}

@app.route("/")
def home():
    return

@app.route("/meeting", methods = ["Get", "Post"])
def meeting():
    if request.method == "Get":
        try:
            data = cur.execute("SELECT * FROM meeting")
            
            return jsonify(data)
        except:
            return "Server side error", 501
        
    if request.method == "Post":
        return