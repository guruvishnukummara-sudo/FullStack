import mysql.connector 
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vishnu@9999",
        database="logaudit_db"
    )