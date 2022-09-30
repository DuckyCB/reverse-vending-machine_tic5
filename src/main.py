from datetime import datetime

from welcome import welcome
from camera import Camera, save_picture
from sensor import sensor
from rotation import rotation

from led_sensor import ObjectDetector


show_camera = True
barcode_in_image = True


def main():
    welcome()
    obj_detector = ObjectDetector(sensor_pin=17)
    while True:
        if obj_detector.read_input():
            camera = Camera()
            bottle = True
            while bottle:
                frame, barcode = camera.barcode_scanner(
                    show_camera, barcode_in_image)
                if barcode is not None:
                    time_now = datetime.now()
                    current_time = time_now.strftime("%d_%m_%Y-%H_%M_%S")
                    save_picture(frame, current_time, barcode)
                    # save bottle to db
                else:
                    rotation()
                if frame is None:
                    camera.release()
                    break
                # the rotation is complete and the bottle has no barcode
                if False:
                    bottle = False
            camera.release()


if __name__ == '__main__':
    main()
