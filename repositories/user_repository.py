from typing import Any
from repositories.db import get_pool
from psycopg.rows import dict_row


def get_userid_by_email(email: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT
                            userID
                        FROM
                            users
                        WHERE email = %s
                        ''', [email])
            result = cur.fetchone()
            if result is not None:
                return result[0]
    return None

def validate_user(email: str, password: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT
                            password
                        FROM
                            users
                        WHERE email = %s
                        ''', [email])
            result = cur.fetchone()
            if result is None:
                # The email does not exist in the database
                return False
            stored_password = result[0]
            return stored_password == password

def does_username_exist(email: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT
                            email
                        FROM
                            users
                        WHERE email = %s
                        ''', [email])
            userid = cur.fetchone()
            return userid is not None


def create_user(email: str, password: str) -> dict[str, Any]:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO app_user (email, password)
                        VALUES (%s, %s)
                        RETURNING userid
                        ''', [first_name, password]
                        )
            userid = cur.fetchone()
            if userid is None:
                raise Exception('failed to create user')
            return {
                'userid': userid,
                'first_name': first_name
            }


def get_user_by_username(username: str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            userid,
                            first_name,
                            password AS hashed_password
                        FROM
                            users
                        WHERE first_name = %s
                        ''', [first_name])
            user = cur.fetchone()
            return user


def get_user_by_id(userid: int) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            userid,
                            first_name
                        FROM
                            users
                        WHERE userid = %s
                        ''', [userid])
            user = cur.fetchone()
            return user