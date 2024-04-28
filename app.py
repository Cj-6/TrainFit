from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session, abort


from repositories import user_repository, workout_repo
from repositories.food_repo import *
from repositories.workout_repo import *

load_dotenv()


app = Flask(__name__)
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
    #check to see if you can just get an id or something so that it only passes the id to the session
    return render_template('nutrition.html', active_page='nutrition')



@app.get('/workout')
def workout():
    userid = session.get('user_id')
    date = request.args.get('date')
    print(userid, date)  
    workouts = workout_repo.get_workout_by_userid_and_date(userid, date)

    return render_template('workout.html', active_page = 'workout', workouts=workouts )


@app.get('/profile')
def profile():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('signin'))
    
    user = user_repository.get_user_by_id(user_id)
    if user is None:
        return redirect('error.html', message='User not found')
    return render_template('profile.html', name=user['first_name'])

@app.get('/signin')
def signin():
    return render_template('signin.html', active_page='signin')

@app.post('/signin')
def signin_post():
    email = request.form.get('email')
    password = request.form.get('password')
    if user_repository.validate_user(email, password):
        # The email and password are valid, create a new session
        session['userid'] = user_repository.get_user_id_by_email(email)
        # Redirect the user to the profile page
        return redirect(url_for('profile'))
    # The email or password is invalid, show an error message
    return render_template('signin.html', error='Invalid email or password')


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

@app.get('/createFood')
def create_food():
    return render_template('createFood.html')


@app.get("/chat")
def chat():
    return render_template("chat.html")




@app.post('/createFoodPost')
def create_food_post():
    name = request.form.get('name')
    calories = request.form.get('calories')
    total_fat = request.form.get('total-fat')
    saturated_fat = request.form.get('saturated-fat')
    trans_fat = request.form.get('trans-fat')
    cholesterol = request.form.get('cholesterol')
    sodium = request.form.get('sodium')
    carbohydrates = request.form.get('carbohydrates')
    sugars = request.form.get('sugars')
    protein = request.form.get('protein')
    

    return render_template('foodInfo.html')

@app.post('/signup')
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        abort(400)
    does_user_exist = user_repository.does_username_exist(username)
    if does_user_exist:
        abort(400)
    user_repository.create_user(username)
    return redirect('/profile.html')
