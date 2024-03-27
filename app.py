from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.get('/workout')
def workout():
    return render_template('workout.html')

@app.get('/profile')
def profile():
    return render_template('profile.html')

@app.get('/signin')
def signin():
    return render_template('signin.html')