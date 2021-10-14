import mysql.connector

def db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='Marshall',
        password='Allstar77'
    )
    return db
