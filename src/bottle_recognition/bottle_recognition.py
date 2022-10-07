from typing import Union
from bottle_recognition.camera import Camera
from bottle_recognition.motor_driver import MotorDriver
import numpy as np
from datetime import datetime
from time import perf_counter


def get_barcode(camera: Camera, show_camera: bool=True):
    for _ in range(4):
        frame, barcode = camera.read_barcode()
        if show_camera:
            camera.display_img(frame, barcode)
        if barcode is not None:
            return barcode, frame
    return None, None


def rotate(motor_driver: MotorDriver, camera: Union[Camera, None], show_camera: bool=True):
    motor_driver.start_motors()

    start = perf_counter()
    current_time = perf_counter()
    while current_time - start < 1:
        if show_camera and Camera is not None:
            _, frame = camera.read_frame()
            camera.display_img(frame, None)
        current_time = perf_counter()
    
    motor_driver.stop_motors()



def start_camera() -> Camera:
    return Camera()


def init_motor_driver() -> MotorDriver:
    motor_driver = MotorDriver()
    print("Motor driver initialized")
    return motor_driver



def release_camera(camera: Camera) -> None:
    camera.release()


def save_data(camera: Camera, frame: np.array, barcode: str) -> None:
    current_time = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
    camera.save_picture(frame, current_time, barcode)
    