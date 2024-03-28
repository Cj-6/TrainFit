from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'bigsecretvibes'

@app.get('/')
def index():
    session['num_exercises'] = 3
    return render_template('index.html', active_page='home')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html', active_page='nutrition')

@app.get('/workout')
def workout():
    return render_template('workout.html', num_exercises=session.get('num_exercises', 3), active_page='workout')


@app.get('/profile')
def profile():
    return render_template('profile.html', active_page='profile')

@app.get('/signin')
def signin():
    return render_template('signin.html', active_page='signin'))

@app.route('/add_exercise', methods=['POST'])
def add_exercise():
    session['num_exercises'] = session.get('num_exercises', 3) + 1
    return redirect(url_for('workout'))

