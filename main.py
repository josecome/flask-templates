from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    msg = "Welcome from Flask, you in home page!"
    return render_template('home.html', msg=msg)




