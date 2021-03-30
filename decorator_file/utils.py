from config import(DATABASE, USER, PASSWORD, HOST, PORT)
import psycopg2

def connection1():
    conn = psycopg2.connect(database = DATABASE, user = USER, password = "loki.", host = HOST, port = PORT)
    if conn:
        cur = conn.cursor()
        return conn, cur
    else:
        return 'connection is not done'
        