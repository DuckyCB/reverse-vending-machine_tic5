import RPi.GPIO as GPIO


def setup_detector(sensor_pin: int) -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor_pin, GPIO.IN)


class ObjectDetector:
    _instance = None

    def __new__(cls, sensor_pin: int = 17):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, sensor_pin: int = 17):
        self.sensor_pin = sensor_pin
        setup_detector(sensor_pin)

    def read_input(self) -> int:
        """Reads input from sensor module in raspberry pi.

        :return:
        1 if an object is detected 0 otherwise.
        """
        return GPIO.input(self.sensor_pin)
