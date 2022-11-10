import requests
from objects.Bottle import Bottle
from db.db_controller import *
import cv2


def test_backend_connection():
    x = requests.get('http://localhost:3000/')
    print(x.text)
    y = requests.post('http://localhost:3000/', json={'key': 'python post'})
    print(y.text)
    print('end')


def test_save_data():
    bottle1 = Bottle(123456789, 10, '01/01/01', 'fabri')
    bottle2 = Bottle(987654321, 11, '02/02/02', 'juan')
    bottle3 = Bottle(543216789, 12, '03/03/03', 'germen')
    save_bottle(bottle1)
    save_bottle(bottle2)
    save_bottle(bottle3)


def test_get_saved_data():
    bottles = get_all_bottles()
    print(bottles)


def camera_test():
    camera = cv2.VideoCapture(0)

    camera.set(cv2.CAP_PROP_FPS, 30.0)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    ret, frame = camera.read()
    while True:
        ret, frame = camera.read()
        cv2.imshow('Camera test', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test_save_data()
    # camera_test()
    # test_save_data()
    # generate_tables()
    # test_get_saved_data()
