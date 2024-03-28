from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html', active_page='home')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html', active_page='nutrition')

@app.get('/workout')
def workout():
    return render_template('workout.html', active_page='workout')

@app.get('/profile')
def profile():
    return render_template('profile.html', active_page='profile')

@app.get('/signin')
def signin():
    return render_template('signin.html', active_page='signin')
