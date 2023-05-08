from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Word!"

@app.route("/meetings")
def meetings():
    return {"pic": 1, "Location": "Östermalm", "Time": "13:13", "Description": "Getting drunk with the bois"}