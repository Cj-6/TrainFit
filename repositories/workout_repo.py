from repositories.db import get_pool
from psycopg.rows import dict_row

def get_workout_by_userid_and_date(userid, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM workout where userid = %s and date = %s', [userid, date])
            workouts = cursor.fetchall()
        return workouts

# base function add as needed and fix what you need