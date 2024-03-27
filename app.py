from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.get('/workout')
def nutrition():
    return render_template('workout.html')