# from datetime import datetime
import RPi.GPIO as GPIO
# from object_detection.led_sensor import ObjectDetector

from welcome import welcome
# from camera import Camera, save_picture
# from object_detection.led_sensor import ObjectDetector
from bottle_recognition.bottle_recognition import get_barcode, rotate_and_detect, start_camera, init_motor_driver, release_camera, save_picture
from object_detection.object_detection import await_no_obj_detection, await_obj_detection, init_led_sensor, init_scale, detect_weight
# from rotation import MotorDriver
# from time import sleep
from db.db_controller import save_bottle
from objects.Bottle import Bottle
from datetime import datetime

show_camera = True
barcode_in_image = True


def main():
    try:
        GPIO.cleanup()
        welcome()
        motor_driver = init_motor_driver()
        detector = init_led_sensor(sensor_pin=17)
        scale = init_scale(sck=6, dt=5)
        threshold = 10
        while True:
            await_obj_detection(detector, scale, threshold)

            camera = start_camera()
            barcode = None
            i = 0
            barcode, frame = get_barcode(camera, show_camera)
            while i < 50 and barcode is None:
                # rotate(motor_driver, camera, show_camera)
                barcode, frame = rotate_and_detect(
                    motor_driver, camera, show_camera)
                i += 1

            if barcode is not None:
                weight = detect_weight(scale)
                print(barcode, 'success')
                current_time = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
                save_picture(camera, frame, barcode, current_time)
                bottle = Bottle(barcode.data, weight, current_time, 'user_hardcoded')
                save_bottle(bottle)

            release_camera(camera)
            await_no_obj_detection(detector, scale, threshold)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('\n','KeyboardInterrupt')


if __name__ == '__main__':
    main()
