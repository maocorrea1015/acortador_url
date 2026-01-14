import pymysql
import os

def conectar_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "acortador"),
        cursorclass=pymysql.cursors.DictCursor
    )
