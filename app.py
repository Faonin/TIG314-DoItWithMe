from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return

@app.route("/meetings", methods = ["Get", "Post"])
def meetings():
    if request.method == "Get":
        return jsonify({"pic": 1, "Location": "Östermalm", "Time": "2023-05-08 13:13", "Description": "Getting drunk with the bois"})
    
    if request.method == "Post":
        return