import RPi.GPIO as GPIO
from lib.hx711 import HX711


referenceUnit = 430


def setup_scale(sck: int, dt: int) -> HX711:
    print("setting up scale")
    hx = HX711(sck, dt)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(referenceUnit)
    hx.reset()
    hx.tare()
    print("scale setup done")

    return hx


class Scale:
    _instance = None

    def __new__(cls, sck: int = 6, dt: int = 5):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, sck: int = 6, dt: int = 5):
        self.sck = sck
        self.dt = dt
        self.hx711 = setup_scale(sck, dt)

    def read_input(self) -> float:
        return max(0, self.hx711.get_weight())
