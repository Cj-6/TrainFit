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
            cursor.execute("SELECT * FROM food WHERE name ILIKE %s", ('%' + search_term + '%',))
            return cursor.fetchall() 

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


