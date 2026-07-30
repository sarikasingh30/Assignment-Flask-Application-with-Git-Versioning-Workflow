from flask import Flask, jsonify
 
app = Flask(__name__)
 
votes={}

# ---------- Task 1: Basic Flask Application ----------
 
@app.route("/")
def home():
    return "Welcome to the App"
 
 
@app.route("/health")
def health():
    return "App is running"
 

 
# ---------- Task 3 Feature Implementation => (Version 1): Voting endpoints ----------
 
@app.route("/vote/<name>")
def vote(name):
    # .get(name, 0) returns 0 if the candidate has never been voted for before,
    # so the very first vote correctly starts the count at 1
    votes[name] = votes.get(name, 0) + 1
    return jsonify({
        "message": f"Vote recorded for {name}",
        "candidate": name,
        "votes": votes[name]
    })
 
 
@app.route("/results")
def results():
    return jsonify(votes)
 

 # ---------- Task 4: Version 2 Enhancement: New endpoint ----------
 
@app.route("/reset")
def reset():
    votes.clear()
    return jsonify({"message": "All votes have been reset"})
 

 