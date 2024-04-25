from repositories.db import get_pool
from psycopg.rows import dict_row

def get_all_foods():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM foods')
        return cursor.fetchall()

# base function add as needed and fix what you need
