import requests
from objects.Bottle import Bottle
from db.db_controller import *
# import cv2
import datetime

host = 'localhost'
port = 8000

def test_backend_connection():
    x = requests.get(f'http://{host}:{port}/bottleOG')
    print(x.text)
    # y = requests.post('http://localhost:3000/', json={'key': 'python post'})
    # print(y.text)
    print('end')

def fetch_bottleOG():
    bottleOGs = requests.get(f'http://{host}:{port}/bottleOG').json()
    update_bottleOGs(bottleOGs)


def save_local_data():
    bottles = get_all_bottles_not_in_backend()
    requests.post(f'http://{host}:{port}/bottle', json=bottles)
    # print(bottles)


def test_save_data():
    bottle1 = Bottle("8934792374", 10, datetime.datetime(2001, 1, 1), 'fabri')
    bottle2 = Bottle("8934792374", 11, datetime.datetime(2002, 2, 2), 'juan')
    bottle3 = Bottle("9837988", 12, datetime.datetime(2003, 3, 3), 'germen')
    save_bottle(bottle1)
    save_bottle(bottle2)
    save_bottle(bottle3)


def test_get_saved_data():
    bottles = get_all_bottles()
    print(bottles)


# def camera_test():
#     camera = cv2.VideoCapture(0)

#     camera.set(cv2.CAP_PROP_FPS, 30.0)
#     camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
#     camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
#     camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#     camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#     ret, frame = camera.read()
#     while True:
#         ret, frame = camera.read()
#         cv2.imshow('Camera test', frame)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
#     camera.release()
#     cv2.destroyAllWindows()


if __name__ == '__main__':
    # test_save_data()
    # generate_tables()
    # fetch_bottleOG()
    # camera_test()
    # test_save_data()
    save_local_data()
    # test_get_saved_data()
    # test_backend_connection()
