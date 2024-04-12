from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'bigsecretvibes'


# This is a test dictionary for the food items
food_dict = {
    'apple': {
        'calories': 52,
        'total_fat': 0.2,
        'saturated_fat': 0,
        'trans_fat': 0,
        'cholesterol': 0,
        'sodium': 1,
        'total_carbohydrates': 14,
        'sugars': 10,
        'protein': 0.3
    },
    'banana': {
        'calories': 96,
        'total_fat': 0.2,
        'saturated_fat': 0,
        'trans_fat': 0,
        'cholesterol': 0,
        'sodium': 1,
        'total_carbohydrates': 23,
        'sugars': 12,
        'protein': 1.2
    },
    'orange': {
        'calories': 43,
        'total_fat': 0.1,
        'saturated_fat': 0,
        'trans_fat': 0,
        'cholesterol': 0,
        'sodium': 1,
        'total_carbohydrates': 9,
        'sugars': 7,
        'protein': 0.9
    },
    'avocado': {
        'calories': 520,
        'total_fat': 3,
        'saturated_fat': 1,
        'trans_fat': 2,
        'cholesterol': 13,
        'sodium': 120,
        'total_carbohydrates': 33,
        'sugars': 35,
        'protein': 2
    },
    'grapes': {
        'calories': 69,
        'total_fat': 0.2,
        'saturated_fat': 0,
        'trans_fat': 0,
        'cholesterol': 0,
        'sodium': 1,
        'total_carbohydrates': 18,
        'sugars': 16,
        'protein': 0.6
    },
    'chicken breast': {
        'calories': 165,
        'total_fat': 3.6,
        'saturated_fat': 1,
        'trans_fat': 2,
        'cholesterol': 13,
        'sodium': 120,
        'total_carbohydrates': 0,
        'sugars': 0,
        'protein': 31
    }
}



@app.get('/')
def index():
    session['num_exercises'] = 3
    return render_template('index.html', active_page='home')



@app.get('/nutrition')
def nutrition():
    return render_template('nutrition.html', active_page='nutrition')


@app.get('/addFood')
def add_food():
    return render_template('addFood.html', current_page='addFood', active_page='nutrition', results={})

@app.post('/nutrition')
def save_food():
    # Get the food and relevant info for the food item
    #check to see if you can just get an id or something so that it only passes the id to the session
    return render_template('nutrition.html', active_page='nutrition')



@app.get('/workout')
def workout():
    return render_template('workout.html', active_page = 'workout')


@app.get('/profile')
def profile():
    return render_template('profile.html', active_page='profile')

@app.get('/signin')
def signin():
    return render_template('signin.html', active_page='signin')

@app.get('/addWorkout')
def add_exercise():
    return render_template('addWorkout.html')

print('test')