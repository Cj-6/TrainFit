from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session, abort, g
from flask_bcrypt import Bcrypt

from repositories import user_repository, workout_repo
from repositories.food_repo import *
from repositories.workout_repo import *

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'bigsecretvibes'

@app.get('/')
def index():
    return render_template('index.html', active_page='home')

@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html', active_page='nutrition')

@app.get('/foodInfo')
def food_info():
    food = get_all_foods()
    return render_template('foodInfo.html', current_page='foodInfo', active_page='nutrition', food=food)

@app.get('/foodInfo/<food_id>')
def food_info_by_id(food_id):
    food = get_food_by_id(food_id)
    return render_template('foodInfo.html', current_page='foodInfo', active_page='nutrition', food=food)

@app.post('/nutrition')
def save_food():
    # Get the food and relevant info for the food item
    # check to see if you can just get an id or something so that it only passes the id to the session
    return render_template('nutrition.html', active_page='nutrition')

@app.get('/workout')
def workout():
    userID = session.get('userID')
    date = request.args.get('date')
    print(userID, date)
    workouts = workout_repo.get_workout_by_userID_and_date(userID, date)  # corrected function name
    return render_template('workout.html', active_page='workout', workouts=workouts)

@app.get('/profile')
def profile():
    if 'userID' in session:
        return render_template('profile.html')
    return redirect(url_for('signin'))

@app.get('/signin')
def signin():
    return render_template('signin.html', active_page='signin')

@app.get('/signup')
def signup():
    return render_template('signup.html', active_page='signup')

@app.post('/signin')
def signin_post():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400)
    user = user_repository.get_user_by_username(email)
    if user is None:
        abort(401)
    if not bcrypt.check_password_hash(user['hashed_password'], password):
        abort(401)
    session['userID'] = user['userID']
    return redirect('/profile')

@app.get('/signout')
def signout():
    session.pop('userID', None)
    return redirect(url_for('index'))

@app.get('/addWorkout')
def add_exercise():
    return render_template('addWorkout.html', active_page='workout')

@app.get('/search')
def search():
    q = request.args.get('q')
    results = {}
    if q:
        results = search_food(q)
    return render_template("searchResults.html", results=results)

@app.get('/myFoods')
def show_my_foods():
    return render_template('myFoods.html')

@app.get('/addFood')
def add_food():
    return render_template('createNewFood.html')

@app.get("/chat")
def chat():
    return render_template("chat.html", active_page='chat')

@app.post('/createFoodPost')
def create_food_post():
    food_data = {
        'name': request.form.get('name'),
        'calories': request.form.get('calories'),
        'total_fat': request.form.get('total_fat'),
        'saturated_fat': request.form.get('saturated_fat'),
        'trans_fat': request.form.get('trans_fat'),
        'cholesterol': request.form.get('cholesterol'),
        'sodium': request.form.get('sodium'),
        'carbohydrates': request.form.get('carbohydrates'),
        'sugars': request.form.get('sugars'),
        'protein': request.form.get('protein')
    }
    new_food = create_food(food_data)
    return render_template('foodInfo.html', food=food_data)

@app.post('/signup')
def signup_account():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    if not email or not password or not confirm_password or password != confirm_password:
        abort(400)
    does_user_exist = user_repository.does_email_exist(email)
    if does_user_exist:
        abort(400)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user_repository.create_user(email, hashed_password)
    return redirect(url_for('profile'))