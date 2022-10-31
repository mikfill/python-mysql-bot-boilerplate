from time import sleep
import mysql.connector
from mysql.connector import Error
from db_config import DB_HOST, DB_USER, DB_USER_PASSWORD, DB_NAME


def create_database():
    """Create database with selected name return name of database in string format
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_USER_PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"DROP DATABASE IF EXISTS `{DB_NAME}`;CREATE DATABASE {DB_NAME};")
            print(f"Database {DB_NAME} created")    
    except Error as e:
        print("Error while connecting to MySQL", e)


def connect_to_db():
    """
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_USER_PASSWORD
        )
        if connection.is_connected():
            return connection
    
    except Error as e:
        print("Error while connecting to MySQL", e)


def create_tables():
    """Connect to database and create tables for user and sentences
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(r"""
# Users
    DROP TABLE IF EXISTS `users`;
    CREATE TABLE `users` (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        user_id BIGINT UNSIGNED NOT NULL DEFAULT 0,
        first_name VARCHAR(64) NULL DEFAULT '',
        last_name VARCHAR(64) NULL DEFAULT '',
        user_name VARCHAR(64) NOT NULL DEFAULT '',
        level TINYINT UNSIGNED NOT NULL DEFAULT 1,
        age TINYINT UNSIGNED NULL,
        PRIMARY KEY (id));
# Sentences
    DROP TABLE IF EXISTS `sentences`;
    CREATE TABLE `sentences` (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        level TINYINT UNSIGNED NOT NULL,
        text TEXT NOT NULL,
        PRIMARY KEY (id));
        """)

    print("Tables users and sentences created")


def fill_sentences_table():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute(r"""
    INSERT INTO `sentences`(id,level,text)
    VALUES 
        (1,2,"When my time comes. Forget the wrong that I've done."),
        (2,3,"In a hole in the ground there lived a hobbit."),
        (3,2,"The sky the port was the color of television, tuned to a dead channel."),
        (4,1,"I love the smell of napalm in the morning."),
        (5,1,"The man in black fled across the desert, and the gunslinger followed."),
        (6,2,"The Consul watched as Kassad raised the death wand."),
        (7,3,"If you want to make enemies, try to change something."),
        (8,2,"We're not gonna take it. Oh no, we ain't gonna take it. We're not gonna take it anymore."),
        (9,3,"I learned very early the difference between knowing the name of something and knowing something.");
        """)
    
    connection.commit()
    print("Table sentences filled data")


def initialize_db():
    create_database()
    sleep(1)
    create_tables()
    sleep(1)
    fill_sentences_table()