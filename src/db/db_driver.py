import sqlite3
from sqlite3 import Error


def create_connection(db_file='src/db/rvm.db': str):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def close_connection(conn):
    conn.close()


def query_post(conn, query: str):
    cur = conn.cursor()
    res = cur.execute(query)
    conn.commit()


def query_post_data(conn, query: str, data: Bottle[]):
    cur = conn.cursor()
    res = cur.executemany(query, data)
    conn.commit()


def query_get_one(conn, query: str):
    cur = conn.cursor()
    res = cur.execute(query)
    return res.fetchone()


def query_get_all(conn, query: str):
    cur = conn.cursor()
    res = cur.execute(query)
    return res.fetchall()
