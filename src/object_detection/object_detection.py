from object_detection.led_sensor import ObjectDetector


n_of_detections = 10


def init_led_sensor(sensor_pin: int=17) -> ObjectDetector:
    detector = ObjectDetector(sensor_pin)
    print("Led sensor module initialized")
    return detector


def await_obj_state(detector: ObjectDetector, state: str) -> None:
    states_dict = {"no_obj": 0, "obj": 1}

    detections_left = n_of_detections
    while detections_left > 0:
        if detector.read_input() == states_dict[state]:
            detections_left -= 1


def await_obj_detection(detector: ObjectDetector) -> None:
    await_obj_state(detector, "obj")


def await_no_obj_detection(detector: ObjectDetector) -> None:
    await_obj_state(detector, "no_obj")
