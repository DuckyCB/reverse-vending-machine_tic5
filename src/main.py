# from datetime import datetime
import RPi.GPIO as GPIO
# from object_detection.led_sensor import ObjectDetector

from welcome import welcome
# from camera import Camera, save_picture
# from object_detection.led_sensor import ObjectDetector
from bottle_recognition.bottle_recognition import get_barcode, rotate_and_detect, start_camera, init_motor_driver, release_camera, save_data
from object_detection.object_detection import await_no_obj_detection, await_obj_detection, init_led_sensor
# from rotation import MotorDriver
# from time import sleep

show_camera = True
barcode_in_image = True


# def main():
#     GPIO.cleanup()
#     welcome()
#     obj_detector = ObjectDetector(sensor_pin=17)
#     # motor_driver = MotorDriver()
#     while True:
#         print(obj_detector.read_input)
#         if obj_detector.read_input():
#             camera = Camera()
#             bottle = True
#             counter = 0
#             while bottle:
#                 frame, barcode = camera.barcode_scanner(
#                     show_camera, barcode_in_image)
#                 if barcode is not None:
#                     time_now = datetime.now()
#                     current_time = time_now.strftime("%d_%m_%Y-%H_%M_%S")
#                     save_picture(frame, current_time, barcode)
#                     # save bottle to db
#                 else:
#                     # motor_driver.start_motors()
#                     # sleep(.5)
#                     # motor_driver.stop_motors()
#                     counter += 1
#                 if frame is None:
#                     camera.release()
#                     break
#                 # the rotation is complete and the bottle has no barcode
#                 if counter == 20:
#                     bottle = False
#                     print('No barcode found')
#             camera.release()


def main():
    GPIO.cleanup()
    welcome()
    motor_driver = init_motor_driver()
    detector = init_led_sensor(sensor_pin=17)
    while True:
        await_obj_detection(detector)

        camera = start_camera()
        barcode = None
        i = 0
        while i < 50 and barcode is None:
            # barcode, frame = get_barcode(camera, show_camera)
            # rotate(motor_driver, camera, show_camera)
            barcode, frame = rotate_and_detect(motor_driver, camera, show_camera)
            i += 1

        if barcode is not None:
            print(barcode, 'success')
            save_data(camera, frame, barcode)

        release_camera(camera)
        await_no_obj_detection(detector)


if __name__ == '__main__':
    main()
