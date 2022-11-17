from db.db_driver import *
from objects.Bottle import Bottle
from constants import RVM_ID


def generate_tables():
    conn = create_connection()
    # query = 'CREATE TABLE bottle(id INT PRIMARY KEY, barcode VARCHAR(30), weight DOUBLE, date DATE, user, backend BOOLEAN NOT NULL)'
    query = 'CREATE TABLE IF NOT EXISTS BOTTLE_OGS(id INT PRIMARY KEY, barcode VARCHAR(30) NOT NULL, weight DOUBLE NOT NULL, price DOUBLE NOT NULL)'
    query_post(conn, query)
    query = 'CREATE TABLE IF NOT EXISTS BOTTLES(id INTEGER PRIMARY KEY AUTOINCREMENT, bottleOG_id INT, weight DOUBLE, date DATE, user_id INT, backend BOOLEAN NOT NULL, FOREIGN KEY (bottleOG_id) REFERENCES BOTTLE_OGS(id))'
    query_post(conn, query)
    close_connection(conn)


def update_bottleOGs(bottleOGs) -> None:
    conn = create_connection()
    query = 'INSERT INTO BOTTLE_OGS(id, barcode, weight, price) VALUES(?, ?, ?, ?)'
    data = [(bottleOG["id"], bottleOG["barcode"], bottleOG["weight"], bottleOG["price"]) for bottleOG in bottleOGs]

    query_post_data(conn, query, data)

    close_connection(conn)

def save_bottle(bottle: Bottle) -> None:
    conn = create_connection()
    # data = [
    #     (
    #         bottle.rvm,
    #         bottle.id,
    #         bottle.barcode,
    #         bottle.weight,
    #         bottle.date,
    #         bottle.user,
    #         False
    #     )
    # ]
    # print(f'Select id from BOTTLE_OGS WHERE barcode = "{bottle.barcode}"')
    bottleog_id = query_get_one(conn, f'Select id from BOTTLE_OGS WHERE barcode = "{bottle.barcode}"')
    print(bottleog_id)

    if bottleog_id is None:
        close_connection(conn)
        return
    
    bottleog_id = bottleog_id[0]

    print(bottle.id);
    
    data = [(
        bottleog_id,
        bottle.weight,
        bottle.date,
        -1,
        False
    )]
    # query = 'INSERT INTO bottle(id, barcode, weight, rvm, date, user, backend) VALUES(?,?,?,?,?,?,?)'
    query = 'INSERT INTO BOTTLES(bottleOG_id, weight, date, user_id, backend) VALUES(?,?,?,?,?)'
    query_post_data(conn, query, data)
    close_connection(conn)


def get_all_bottles():
    conn = create_connection()
    query = 'SELECT * FROM BOTTLES'
    bottles = query_get_all(conn, query)
    close_connection(conn)
    return bottles


def get_all_bottles_not_in_backend():
    conn = create_connection()
    query = 'SELECT * FROM BOTTLES WHERE backend=false'
    bottles = query_get_all(conn, query)
    close_connection(conn)
    ids = tuple(bottle[0] for bottle in bottles)
    set_all_bottles_as_sent_to_backend(ids)
    bottles_json = [{"id": bottle[0], "bottleOGId": bottle[1], "measuredWeight": bottle[2], "rvmId": RVM_ID} for bottle in bottles]
    return bottles_json


def set_all_bottles_as_sent_to_backend(ids):
    conn = create_connection()
    query = f'UPDATE BOTTLES SET backend = true WHERE id IN {ids}'
    query_post(conn, query)
    close_connection(conn)
