import RPi.GPIO as GPIO

in1 = 24
in2 = 23
en = 25
GPIO.cleanup()


class Motordriver:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        self.p = GPIO.PWM(en, 1000)
        self.p.start(100)

    def start_motors(self):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)

    def stop_motors(self):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

def rotation():
    pass
