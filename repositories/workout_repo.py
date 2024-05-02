from repositories.db import get_pool
from psycopg.rows import dict_row

def get_workout_by_userID_and_date(userID, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM workout where userID = %s and date = %s', [userID, date])
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

def get_workout_details_by_user_and_date(userID, date):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM Workout WHERE userID = %s AND date = %s', [userID, date])
            workouts = cursor.fetchall()
            for workout in workouts:
                cursor.execute('SELECT * FROM exercise WHERE workoutID = %s', [workout['workoutid']])
                exercises = cursor.fetchall()
                for exercise in exercises:
                    cursor.execute('SELECT * FROM set WHERE exerciseID = %s', [exercise['exerciseid']])
                    sets = cursor.fetchall()
                    exercise['sets'] = sets
                workout['exercises'] = exercises

    print(f"Returning workouts: {workouts}")
    return workouts

def create_workout(workout):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO workout (userID, name, date) VALUES (%s, %s, %s) RETURNING workoutid',
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
