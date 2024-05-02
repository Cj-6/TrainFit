import uuid
from repositories.db import get_pool
from psycopg.rows import dict_row

def get_all_foods():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM food')
            return cursor.fetchall()

def search_food(search_term):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor: 
            # first, search for foods that start with the search term
            cursor.execute("SELECT * FROM food WHERE name ILIKE %s LIMIT 5", (search_term + '%',))
            results = cursor.fetchall()

            # if less than 5 results, search for foods that contain the search term but do not start with it
            if len(results) < 5:
                cursor.execute("SELECT * FROM food WHERE name ILIKE %s AND name NOT ILIKE %s LIMIT %s", ('%' + search_term + '%', search_term + '%', 5 - len(results)))
                results += cursor.fetchall()

            return results

def get_food_by_id(food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor: 
            cursor.execute("SELECT * FROM food WHERE foodid = %s", (food_id,))
            return cursor.fetchone()  # fetch the food with the given ID
        
def get_food_creator(food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute("""
            SELECT users.name 
            FROM Food 
            JOIN Users ON Food.createdByID = Users.userID 
            WHERE Food.FoodID = %s
            """, (food_id,))
            return cursor.fetchone()
        
def create_food(food_data, user_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO food 
                                (foodid, name, calories, protein, total_fat, saturated_fat, trans_fat, 
                                cholesterol, sodium, carbohydrates, sugars, createdbyid) 
                            VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                            (str(uuid.uuid4()), food_data['name'], food_data['calories'], food_data['total_fat'],  
                            food_data['saturated_fat'], food_data['trans_fat'], food_data['cholesterol'], 
                            food_data['sodium'], food_data['carbohydrates'], food_data['sugars'], food_data['protein'], user_id))
            conn.commit()


def create_meal(meal_name, userID, food_id, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO Meal 
                                (meal_name, userID, FoodID, date) 
                            VALUES 
                                (%s, %s, %s, %s)''', 
                            (meal_name, userID, food_id, date))
            conn.commit()
            conn.close()


def get_meal_by_user_and_date(meal_name, date, user_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT Meal.*, Food.* 
                FROM Meal 
                INNER JOIN Food ON Meal.FoodID = Food.FoodID
                WHERE Meal.meal_name = %s AND Meal.date = %s AND Meal.userID = %s
            """, (meal_name, date, user_id))
            return cursor.fetchall()

def create_comment(comment):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO comments 
                                (comment_text, userID, foodid) 
                            VALUES 
                                (%s, %s, %s)''', 
                            (comment['comment_text'], comment['userID'], comment['foodid']))
            conn.commit()

def delete_comments(food_id, id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM comments WHERE foodid = %s AND commentid = %s', (food_id, id))
            conn.commit()

def get_comments(food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM comments WHERE foodid = %s', (food_id,))
            return cursor.fetchall()
        
def get_comment_by_id(comment_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM comments WHERE commentid = %s', (comment_id,))
            return cursor.fetchone()

def update_comments(comment, id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            UPDATE comments 
                            SET comment_text = %s
                            WHERE commentid = %s
                            ''', 
                            (comment['comment_text'], id))
            conn.commit()

def get_user_foods(userID):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                SELECT f.foodid, f.name, f.calories, f.total_fat, f.saturated_fat, f.trans_fat,
                       f.cholesterol, f.sodium, f.carbohydrates, f.sugars, f.protein
                FROM food f
                JOIN meal m ON f.foodid = m.foodid
                WHERE m.userID = %s
            ''', (userID,))
            return cursor.fetchall()

def update_food(food):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE food
                SET name = %s, calories = %s, total_fat = %s, saturated_fat = %s,
                    trans_fat = %s, cholesterol = %s, sodium = %s, carbohydrates = %s,
                    sugars = %s, protein = %s
                WHERE foodid = %s
            ''', (food['name'], food['calories'], food['total_fat'], food['saturated_fat'],
                  food['trans_fat'], food['cholesterol'], food['sodium'], food['carbohydrates'],
                  food['sugars'], food['protein'], food['foodid']))
            conn.commit()

def delete_food_by_id(food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM food WHERE foodid = %s', (food_id,))
            conn.commit()