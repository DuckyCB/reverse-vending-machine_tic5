from datetime import datetime
import RPi.GPIO as GPIO

from welcome import welcome
from camera import Camera, save_picture
from led_sensor import ObjectDetector
from rotation import MotorDriver
from time import sleep

show_camera = True
barcode_in_image = True


def main():
    GPIO.cleanup()
    welcome()
    obj_detector = ObjectDetector(sensor_pin=17)
    motor_driver = MotorDriver()
    while True:
        if obj_detector.read_input():
            camera = Camera()
            bottle = True
            counter = 0
            while bottle:
                frame, barcode = camera.barcode_scanner(
                    show_camera, barcode_in_image)
                if barcode is not None:
                    time_now = datetime.now()
                    current_time = time_now.strftime("%d_%m_%Y-%H_%M_%S")
                    save_picture(frame, current_time, barcode)
                    # save bottle to db
                else:
                    motor_driver.start_motors()
                    sleep(.5)
                    motor_driver.stop_motors()
                    counter += 1
                if frame is None:
                    camera.release()
                    break
                # the rotation is complete and the bottle has no barcode
                if counter == 20:
                    bottle = False
                    print('No barcode found')
            camera.release()


if __name__ == '__main__':
    main()
