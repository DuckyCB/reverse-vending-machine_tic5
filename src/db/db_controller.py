from db.db_driver import *


def generate_tables():
    conn = create_connection()
    query = 'CREATE TABLE bottle(id, barcode, weight, rvm, date, user)'
    query_post(conn, query)


def save_bottle(new_bottle):
    conn = create_connection()
    bottle = validate_bottle_data(new_bottle)
    query = f"""INSERT INTO bottle VALUES(
            {bottle.rvm}, 
            {bottle.id}, 
            {bottle.barcode}, 
            {bottle.weight}, 
            {bottle.date}, 
            {bottle.user}
        )"""
    query_post(conn, query)


def validate_bottle_data(bottle):
    return bottle
