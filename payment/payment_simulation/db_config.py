import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gurappa123@9999",
        database="payment_db"
    )
