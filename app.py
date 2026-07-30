from flask import Flask, jsonify
 
app = Flask(__name__)
 
 
# ---------- Task 1: Basic Flask Application ----------
 
@app.route("/")
def home():
    return "Welcome to the App"
 
 
@app.route("/health")
def health():
    return "App is running"
 
 