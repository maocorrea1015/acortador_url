import pymysql

def conectar_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="acortador",
        cursorclass=pymysql.cursors.DictCursor
    )
