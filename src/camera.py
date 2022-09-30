from typing import Any
import cv2 as cv
from pyzbar import pyzbar
import numpy as np
import time


def start_camera():
    print('Starting camera...')
    camera = cv.VideoCapture(1, cv.CAP_DSHOW)
    camera.set(cv.CAP_PROP_FPS, 30.0)
    camera.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('m', 'j', 'p', 'g'))
    camera.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    camera.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
    return camera


class Camera:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.camera = start_camera()

    def barcode_scanner(self, show_camera: bool = True, barcode_in_image: bool = True):
        n = 0
        ret, frame = self.camera.read()
        while ret and n < 4:
            ret, frame = self.camera.read()
            barcode = read_barcodes(frame)
            n += 1
            if show_camera:
                if barcode is not None and barcode_in_image:
                    add_barcode_to_frame(frame, barcode)
                cv.imshow('Barcode/QR code reader', frame)
            if barcode is not None:
                # barcode_info = barcode.data.decode('utf-8')
                return frame, barcode
            if cv.waitKey(1) & 0xFF == 27:
                return None, None
        return frame, None

    def release(self):
        self.camera.release()
        cv.destroyAllWindows()


def read_barcodes(frame: np.array) -> Any | None:
    barcodes = pyzbar.decode(frame)
    # return None if not any(barcodes) else barcodes[0]
    return barcodes[0] if any(barcodes) else None


def add_barcode_to_frame(frame: np.array, barcode) -> np.array:
    x, y, w, h = barcode.rect
    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(frame, barcode, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
    return frame


def save_picture(frame: np.array, current_time: str, barcode: str):
    try:
        cv.imwrite(f"output/{current_time}.jpg", frame)
        with open(f"output/{current_time}.txt", mode='w') as file:
            file.write(barcode + ' ' + current_time)
    except cv.error:
        print('error saving picture')
