import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,  # tu puerto MySQL
        user='root',
        password='root',
        database='ganaderia'
    )
    return conn