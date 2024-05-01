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
        
def create_food(food):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO food 
                                (foodid, name, calories, protein, total_fat, saturated_fat, trans_fat, 
                                cholesterol, sodium, carbohydrates, sugars) 
                            VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                            (str(uuid.uuid4()), food['name'], food['calories'], food['total_fat'],  
                            food['saturated_fat'], food['trans_fat'], food['cholesterol'], 
                            food['sodium'], food['carbohydrates'], food['sugars'], food['protein']))
            conn.commit()


def create_meal(meal_name, user_id, food_id, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO Meal 
                                (meal_name, userID, FoodID, date) 
                            VALUES 
                                (%s, %s, %s, %s)''', 
                            (meal_name, user_id, food_id, date))
            conn.commit()
            conn.close()

def create_comment(comment, user_id, food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO comments 
                                (comment_text, user_id, food_id) 
                            VALUES 
                                (%s, %s, %s)''', 
                            (comment, user_id, food_id))
            conn.commit()
            conn.close()

def get_comments(food_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM Comment WHERE FoodID = %s', (food_id,))
            return cursor.fetchall()      
def delete_comments(food_id, comment_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM Comment WHERE FoodID = %s AND commentID = %s', (food_id, comment_id))
            conn.commit()
            conn.close()
