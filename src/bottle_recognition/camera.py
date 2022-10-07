import cv2 as cv
import numpy as np
from pyzbar import pyzbar


def start_camera() -> None:
    print('Starting camera...')
    camera = cv.VideoCapture(1, cv.CAP_DSHOW)
    camera.set(cv.CAP_PROP_FPS, 30.0)
    camera.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('m', 'j', 'p', 'g'))
    camera.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    camera.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
    camera.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
    return camera

def append_barcode_to_frame(frame: np.array, barcode) -> np.array:
    x, y, w, h = barcode.rect
    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(frame, barcode, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
    return frame


def read_barcode(frame: np.array):
    barcodes = pyzbar.decode(frame)
    return barcodes[0] if len(barcodes) > 0 else None


class Camera:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        self.camera = start_camera()


    def read_frame(self):
        return self.camera.read()


    def read_barcode(self):
        ret, frame = self.read_frame()
        if not ret:
            return None, None

        barcode = read_barcode(frame)
        return frame, barcode


    def display_img(self, frame: np.array, barcode):
        if barcode is not None:
            frame = append_barcode_to_frame(frame, barcode)
        cv.imshow('Barcode/QR code reader', frame)

    
    def release(self):
        self.camera.release()
        cv.destroyAllWindows()

    
    def save_picture(self, frame: np.array, current_time: str, barcode: str):
        try:
            cv.imwrite(f"output/{current_time}.jpg", frame)
            with open(f"output/{current_time}.txt", mode='w') as fp:
                fp.write(f"{barcode} {current_time}")
                print("data successfully saved")
        except cv.error:
            print('error saving picture')