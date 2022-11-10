from time import perf_counter
from typing import Union

import numpy as np

from bottle_recognition.camera import Camera
from bottle_recognition.motor_driver import MotorDriver


def get_barcode(camera: Camera, show_camera: bool = True):
    for _ in range(4):
        frame, barcode = camera.read_barcode()
        if show_camera:
            camera.display_img(frame, barcode)
        if barcode is not None:
            return barcode, frame
    return None, None


def rotate_and_detect(motor_driver: MotorDriver, camera: Camera, show_camera: bool = True):
    motor_driver.start_motors()

    # start = perf_counter()
    # current_time = perf_counter()
    # while current_time - start < 0.5:
    #     if show_camera and Camera is not None:
    #         _, frame = camera.read_frame()
    #         camera.display_img(frame, None)
    #     current_time = perf_counter()
    barcode, frame = delay_and_detect(.5, camera, show_camera)

    motor_driver.stop_motors()

    return (barcode, frame) if barcode is not None else delay_and_detect(.5, camera, show_camera)


def delay_and_detect(time: float, camera: Camera, show_camera: bool) -> None:
    start = perf_counter()
    current_time = perf_counter()
    while current_time - start < time:
        barcode, frame = get_barcode(camera, show_camera)
        print(f"barcode: {barcode}")
        if barcode is not None:
            return barcode, frame
        current_time = perf_counter()

    return None, None


def start_camera() -> Camera:
    return Camera()


def init_motor_driver() -> MotorDriver:
    motor_driver = MotorDriver()
    print("Motor driver initialized")
    return motor_driver


def release_camera(camera: Camera) -> None:
    camera.release()


def save_picture(camera: Camera, frame: np.array, barcode: str, time: str) -> None:
    camera.save_picture(frame, time, barcode)
