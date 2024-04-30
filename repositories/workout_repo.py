from repositories.db import get_pool
from psycopg.rows import dict_row

def get_workout_by_userid_and_date(userid, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM workout where userid = %s and date = %s', [userid, date])
            workouts = cursor.fetchall()
        return workouts
    
def create_exercise(exercise):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO exercise (workoutid, exerciseName) VALUES (%s, %s) RETURNING exerciseid',
                [exercise['workoutID'], exercise['name']]
            )
            exercise_id = cursor.fetchone()[0]
        conn.commit()
    return exercise_id

def create_workout(workout):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO workout (userid, name, date) VALUES (%s, %s, %s) RETURNING workoutid',
                [workout['userID'], workout['name'], workout['date']]
            )
            workout_id = cursor.fetchone()[0]
        conn.commit()
    return workout_id

def create_set(set):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO set (exerciseID, weight, rpe, note, reps) VALUES (%s, %s, %s, %s, %s) RETURNING setid',
                [set['exerciseID'], set['weight'], set['rpe'], set['note'], set['reps']]
            )
            set_id = cursor.fetchone()[0]
        conn.commit()
    return set_id
