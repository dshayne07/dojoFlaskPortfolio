from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def home():
    return render_template("projects.html")

@app.route("/about")
def home():
    return render_template("about.html")

app.run(debug=True)