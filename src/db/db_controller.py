from db.db_driver import *


def generate_tables():
    conn = create_connection()
    query = 'CREATE TABLE bottle(id, barcode, weight, rvm, date, user, backend)'
    query_post(conn, query)
    close_connection(conn)


def save_bottle(bottle):
    conn = create_connection()
    data = [
        (
            bottle.rvm,
            bottle.id,
            bottle.barcode,
            bottle.weight,
            bottle.date,
            bottle.user,
            False
        )
    ]
    query = 'INSERT INTO bottle(id, barcode, weight, rvm, date, user, backend) VALUES(?,?,?,?,?,?,?);'
    query_post_data(conn, query, data)
    close_connection(conn)


def get_all_bottles():
    conn = create_connection()
    query = 'SELECT * FROM bottle'
    bottles = query_get_all(conn, query)
    close_connection(conn)
    return bottles


def get_all_bottles_not_in_backend():
    conn = create_connection()
    query = 'SELECT * FROM bottle WHERE backend=false'
    bottles = query_get_all(conn, query)
    close_connection(conn)
    return bottles

# TODO: Change values where backend=false to true
def set_all_bottles_as_sent_to_backend():
    # conn = create_connection()
    # query = 'SELECT * FROM bottle WHERE backend=false'
    # bottles = query_get_all(conn, query)
    # for bottle in bottles:
    #     bottle.backend = True
    
    # close_connection(conn)
    # return bottles
    pass
