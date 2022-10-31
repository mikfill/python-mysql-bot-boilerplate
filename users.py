from db_config import *
from init_db import connect_to_db


def add_new_user(user_id: int, level = 1):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    INSERT INTO users(user_id, level)
    VALUES ({user_id},{level})
        """)
    
    connection.commit()
    print(f"Add new user with id: {user_id}\tlvl:{level}")


def get_user_by_id(user_id: int) -> bool:
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    SELECT user_id FROM users
    WHERE user_id = {user_id}
        """)

    result = cursor.fetchone()
    return False if result is None else True
 

def get_all_users() -> list:
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    SELECT id, user_id, level AS lvl FROM users
        """)
    
    result = cursor.fetchall()
    print(f"{result}")
    return result


def get_users_with_lvl(level: int) -> list:
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    SELECT id, user_id, level FROM users 
    WHERE level = {level}
    ORDER BY id
        """)
    
    result = cursor.fetchall()
    print(f"{result}")
    return result 


def get_user_level(user_id: int) -> int:
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    SELECT level FROM users 
    WHERE user_id = {user_id}
        """)
    
    result = cursor.fetchone()
    print(f"{result[0]}")
    return result[0]


def update_user_level(user_id: int, level: int):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    UPDATE users SET level='{level}'
    WHERE user_id = {user_id}
        """)
    
    connection.commit()

    print(f"Level for user {user_id} updated on {level}")


def update_user_first_name(user_id: int, first_name: str):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    UPDATE users SET first_name = '{first_name}'
    WHERE user_id = {user_id}
        """)
    
    connection.commit()

    print(f"First name for user {user_id} updated on {first_name}")
    

def update_user_last_name(user_id: int, last_name: str):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    UPDATE users SET last_name = '{last_name}'
    WHERE user_id = {user_id}
        """)
    
    connection.commit()

    print(f"Last name for user {user_id} updated on {last_name}")
    

def update_user_user_name(user_id: int, user_name: str):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    UPDATE users SET user_name = '{user_name}'
    WHERE user_id = {user_id}
        """)
    
    connection.commit()

    print(f"User name for user {user_id} updated on {user_name}")


def update_user_age(user_id: int, age: int):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    UPDATE users SET age = {age}
    WHERE user_id = {user_id}
        """)
    
    connection.commit()

    print(f"Age for user {user_id} updated on {age}")


def boiler_plate():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(rf"""
    
        """)
    
    connection.commit()

    print(f"")
    pass



