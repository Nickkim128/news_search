from flask import Flask, render_template

app = Flask(__name__)

#renders the home page 
@app.route("/")
def homepage():
    return render_template('home.html')