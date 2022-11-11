# import requests
from objects.Bottle import Bottle
from db.db_controller import save_bottle, generate_tables


def test_backend_connection():
    x = requests.get('http://localhost:3000/')
    print(x.text)
    y = requests.post('http://localhost:3000/', json={'key': 'python post'})
    print(y.text)
    print('end')


def test_db():
    bottle = Bottle(123456789, 10, '01/01/01', 'fabri')
    print(str(bottle))
    save_bottle(bottle)


if __name__ == '__main__':
    test_db()
    # generate_tables()
