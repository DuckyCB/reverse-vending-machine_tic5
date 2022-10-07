import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en1 = 25

en2 = 16
in3 = 20
in4 = 21 

class MotorDriver:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en1, GPIO.OUT)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        
        GPIO.setup(in3, GPIO.OUT)
        GPIO.setup(in4, GPIO.OUT)
        GPIO.setup(en2, GPIO.OUT)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        
        self.p1 = GPIO.PWM(en1, 1000)
        self.p1.start(50)

        self.p2 = GPIO.PWM(en2, 1000)
        self.p2.start(50)

    def start_motors(self):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)

    def stop_motors(self):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

if __name__ == '__main__':
    driver = MotorDriver()
    while True:
        driver.start_motors()
        sleep(0.1)
        driver.stop_motors()
        sleep(0.5)