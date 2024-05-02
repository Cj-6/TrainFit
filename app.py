import os
from dotenv import load_dotenv
from flask import Flask, g, render_template, redirect, request, url_for, session, abort, flash
from flask_bcrypt import Bcrypt
from datetime import date as dt

from repositories import user_repository, workout_repo
from repositories.food_repo import *
from repositories.workout_repo import *
from repositories.user_repository import *
from datetime import date

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.getenv('APP_SECRET_KEY')

#index
@app.get('/')
def index():
    userID = session.get('userID')
    return render_template('index.html', active_page='home')


#chat
@app.get("/chat")
def chat():
    return render_template("chat.html", active_page='chat')


#workout get
@app.get('/workout')
def workout():
    userID = session.get('userID')
    date = request.args.get('date')
    if date is None:
        date = dt.today().strftime('%Y-%m-%d')
        return redirect(url_for('workout', date=date))
    workouts= None
    if userID is not None:
        if date is not None:
            workouts = workout_repo.get_workout_details_by_user_and_date(userID, date)
    if not workouts:
        workouts = [{
            'name': 'Template Workout',
            'exercises': [
                {
                    'exercisename': 'Template Press',
                    'sets': [
                        {
                            'weight': '225',
                            'reps': '8',
                            'rpe': '6',
                            'note': 'Lightweight babbbbayyyyy!',
                        },
                        {
                            'weight': '315',
                            'reps': '4',
                            'rpe': '9',
                            'note': 'Elbow was hurting on this set!',
                        },
                        {
                            'weight': '405',
                            'reps': '1',
                            'rpe': '10',
                            'note': 'Just hit a PR!!!',
                        }   
                    ]
                },
                {
                    'exercisename': 'Template Row',
                    'sets': [
                        {
                        'weight': '225',
                        'reps': '8',
                        'rpe': '6',
                        'note': 'Lightweight babbbbayyyyy!',
                    },
                    {
                        'weight': '315',
                        'reps': '4',
                        'rpe': '9',
                        'note': 'Elbow was hurting on this set!',
                    },
                    {
                        'weight': '405',
                        'reps': '1',
                        'rpe': '10',
                        'note': 'Just hit a PR!!!',
                    }
                ]
            }
        ]
    }]
    return render_template('workout.html', active_page='workout', workouts=workouts, date=date)

@app.post('/workout')
def adddate():
    date = request.form.get('calendar')
    if date is None:
        date = dt.today().strftime('%Y-%m-%d')
    return redirect(url_for('workout', date=date))

@app.get('/addWorkout')
def add_exercise():
    if 'userID' not in session:
        return redirect(url_for('signin')) 
    date = dt.today().strftime('%Y-%m-%d')
    return render_template('addWorkout.html', active_page='workout', date=date)

@app.post('/addWorkout')
def submit_workout():
    userID = session.get('userID')
    date = request.form.get('calendar')
    workout_name = request.form.get('workout-name')
    print(userID)
    workout = {
        'name': workout_name,
        'userID': userID,
        'date': date,
    }
    print(workout)
    workoutID = workout_repo.create_workout(workout)
    print(workoutID)
    exercises = []
    for i in range(1, 12): 
        sets = []
        for j in range(1, 12):  
            set_weight = request.form.get(f'exercise-{i}-set-{j}-weight')
            set_reps = request.form.get(f'exercise-{i}-set-{j}-reps')
            set_rpe = request.form.get(f'exercise-{i}-set-{j}-rpe')
            set_text = request.form.get(f'exercise-{i}-set-{j}-text')
            if set_weight or set_reps or set_rpe or set_text:
                sets.append({
                    'weight': set_weight,
                    'rpe': set_rpe,
                    'note': set_text,
                    'reps': set_reps,
                })
        if sets:
            exercise_name = request.form.get(f'exercise-{i}-name')
            exercise = {
                'name': exercise_name,
                'workoutID': workoutID,
            }
            exerciseID = workout_repo.create_exercise(exercise)
            for set in sets:
                set['exerciseID'] = exerciseID
                workout_repo.create_set(set)
            
    return redirect(url_for('workout'))



@app.before_request
def before_request():
    date = request.args.get('date')
    if request.endpoint in ['nutrition', 'food_info', 'workout'] and date is None:
        date = dt.today().strftime('%Y-%m-%d')
        session['date'] = date
    if date is None:
        date = dt.today().strftime('%Y-%m-%d')
    g.date = date

@app.get('/nutrition')
def nutrition():
    date = request.args.get('date')
    if date is None:
        date = dt.today().strftime('%Y-%m-%d')
        return redirect(url_for('nutrition', date=date))

    user_id = session.get('userID')  # Get the user ID from the session
    meals = ['breakfast', 'lunch', 'dinner', 'snack']  # Define the meal names
    meal_data = {}

    # Fetch the meal data for each meal
    for meal_name in meals:
        meal_data[meal_name] = get_meal_by_user_and_date(meal_name, date, user_id)

    return render_template('nutrition.html', active_page='nutrition', date=date, meal_data=meal_data)

#nutrition post
@app.post('/nutrition')
def add_food_to_meal():
    meal_name = session.get('mealName')
    userID = session.get('userID')
    date = request.form.get('date')
    food_id = request.form.get('food_id')
    session['date'] = date

    # Validate meal_name
    if meal_name not in ['breakfast', 'lunch', 'dinner', 'snack']:
        return 'Invalid meal name', 400

    # Validate date and food_id
    if not food_id:
        flash('You must select a food item.', 'danger')
        return redirect(url_for('food_info', mealName=meal_name))
    
    if not date:
        flash('You must select a date.', 'danger')
        return redirect(url_for('food_info_by_id', food_id=food_id))

    create_meal(meal_name, userID, food_id, date)
    flash('Food added successfully!', 'success')
    meal_data = {}
    for meal_name in ['breakfast', 'lunch', 'dinner', 'snack']:
        meal_data[meal_name] = get_meal_by_user_and_date(meal_name, date, userID)
    return render_template('nutrition.html', active_page='nutrition', meal_data=meal_data)

@app.get('/foodInfo')
def food_info():
    meal_name = request.args.get('mealName')
    date = session.get('date', dt.today().strftime('%Y-%m-%d'))
    session['mealName'] = meal_name 
    food = get_all_foods()
    return render_template('foodInfo.html', current_page='foodInfo', active_page='nutrition', food=food, date=date)

@app.get('/foodInfo/<food_id>')
def food_info_by_id(food_id):
    food = get_food_by_id(food_id)
    creator = get_food_creator(food_id)
    comments = get_comments(food_id)
    return render_template('foodInfo.html', current_page='foodInfo', active_page='nutrition', food=food, comments=comments, creator=creator)

@app.get('/createFood')
def get_create_food():
    if 'userID' not in session:
        flash('You must be signed in to add a food.', 'danger')
        return redirect(url_for('signin'))
    date = session.get('date')  # Get the date from the session
    meal_name = session.get('mealName')  # Get the meal name from the session
    return render_template('createFood.html', active_page='nutrition', selected_date=date, meal_name=meal_name)

@app.get('/search')
def search():
    q = request.args.get('q')
    meal_name = request.args.get('mealName')
    results = {}
    if q:
        results = search_food(q)
    return render_template("searchResults.html", results=results, meal_name=meal_name)

@app.get('/myFoods')
def show_my_foods():
    return render_template('myFoods.html')

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
        'protein': request.form.get('protein'),
    }
    user_id = session.get('userID')
    food_data['user_id'] = user_id
    food_data = create_food(food_data, user_id)
    return render_template('foodInfo.html', food=food_data, active_page='nutrition')


#user get
@app.get('/signin')
def signin():
    userID = session.get('userID')
    return render_template('signin.html', active_page='signin')

@app.get('/signup')
def signup():
    return render_template('signup.html', active_page='signup')

@app.get('/profile')
def profile():
    if 'userID' not in session:
        flash('You must be signed in to view your profile.', 'danger')
        return redirect('/')
    userID = session.get('userID')
    user_data = user_repository.get_user_profile_data(userID)
    return render_template('profile.html', user=user_data, active_page='profile')

@app.get('/logout')
def logout():
    flash('You have been successfully signed out.', 'success')
    del session['userID']
    return redirect('/')

@app.get('/editprofile')
def edit_profile():
    if 'userID' not in session:
        return redirect('/')
    
    userID = session.get('userID')
    user = user_repository.get_user_by_id(userID)
    return render_template('editprofile.html', user=user, active_page='profile')


#user post
@app.post('/signup')
def signup_account():
    email = request.form.get('email').lower()
    password = request.form.get('password')
    if not email or not password:
        flash('Email and password are required.', 'danger')
        return redirect(url_for('signup'))
    does_user_exist = user_repository.does_email_exist(email)
    if does_user_exist:
        flash('User with this email already exists.', 'danger')
        return redirect(url_for('signup'))
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user_repository.create_user(email, hashed_password)
    user = user_repository.get_user_by_email(email)
    session['userID'] = user['userID']
    flash('Account created successfully!', 'success')
    return redirect(url_for('profile'))

@app.post('/signin')
def signin_account():
    email = request.form.get('email').lower() 
    password = request.form.get('password')
    user = user_repository.get_user_by_email(email)
    if user is None or not bcrypt.check_password_hash(user['hashed_password'], password):
        flash('Invalid email or password.', 'danger')
        return render_template('signin.html', active_page='signin')  
    else:
        session['userID'] = user['userID']
        flash('You have successfully signed in.', 'success')
        return redirect(url_for('profile'))

@app.post('/editprofile')
def update_profile():
    if 'userID' not in session:
        return redirect('/')

    userID = session.get('userID')
    name = request.form.get('name')
    age = request.form.get('age')
    height = request.form.get('height')
    weight = request.form.get('weight')
    goal = request.form.get('goal')

    if not name or not age or not height or not weight or not goal:
        flash('All fields are required.', 'danger')
        return redirect(url_for('profile'))

    updated_user = user_repository.update_user(userID, name, age, height, weight, goal)
    if updated_user is None:
        flash('An error occurred while updating the profile.', 'danger')
        return redirect(url_for('profile'))
    user_data = user_repository.get_user_profile_data(userID)
    flash('Profile updated successfully!', 'success')
    return render_template('profile.html', user=user_data, active_page='profile')


#comments
@app.post('/foodInfo/<food_id>')
def add_comment(food_id):
    userID = session.get('userID')
    comment_text = request.form.get('comment')
    if not comment_text:
        flash('Comment cannot be empty.', 'danger')
        return redirect(url_for('food_info', food_id=food_id))
    comment = {
        'food_id': food_id,
        'userID': userID,
        'comment_text': comment_text
    }
    create_comment(comment)
    flash('Comment added successfully!', 'success')
    return redirect(url_for('food_info', food_id=food_id))

@app.post('/foodInfo/<food_id>/delete/<comment_id>')
def delete_comment(food_id, comment_id):
    userID = session.get('userID')
    comment = get_comments(food_id)  # Assuming you fetch comments by food_id
    if comment['userID'] != userID:
        flash('You can only delete your own comments.', 'danger')
        return redirect(url_for('food_info', food_id=food_id))
    delete_comments(food_id, comment_id)
    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('food_info', food_id=food_id))
