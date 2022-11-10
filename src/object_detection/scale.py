import RPi.GPIO as GPIO
from hx711 import HX711


referenceUnit = 1

def setup_scale(sck: int, dt: int) -> HX711:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sck, GPIO.IN)
    GPIO.setup(dt, GPIO.IN)

    hx = HX711(sck, dt)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    hx.reset()
    hx.tare()

    return hx


class Scale:
    _instance = None

    def __new__(cls, sck: int = 5, dt: int = 6):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, sck: int = 5, dt: int = 6):
        self.sck = sck
        self.dt = dt
        self.hx711 = setup_scale(sck, dt)
        setup_scale(sck, dt)

    def read_input(self) -> int:
        return self.hx711.get_weight()
