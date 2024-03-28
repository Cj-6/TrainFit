from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'bigsecretvibes'

@app.get('/')
def index():
    session['num_exercises'] = 3
    return render_template('index.html')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.get('/workout')
def workout():
    return render_template('workout.html', num_exercises=session.get('num_exercises', 3))

@app.get('/profile')
def profile():
    return render_template('profile.html')

@app.get('/signin')
def signin():
    return render_template('signin.html')

@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    session['num_exercises'] = session.get('num_exercises', 3) + 1
    return redirect(url_for('workout'))

