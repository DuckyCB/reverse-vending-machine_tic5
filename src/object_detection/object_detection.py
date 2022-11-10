from object_detection.led_sensor import ObjectDetector
from object_detection.scale import Scale


n_of_led_detections = 10
n_of_scale_detections = 5


def init_led_sensor(sensor_pin: int = 17) -> ObjectDetector:
    detector = ObjectDetector(sensor_pin)
    print("Led sensor module initialized")
    return detector


def init_scale(sck: int = 6, dt: int = 5) -> Scale:
    scale = Scale(sck, dt)
    print("Scale module initialized")
    return scale


def detect_weight(scale: Scale) -> float:
    return scale.read_input()


def object_placed(scale: Scale, threshold: float):
    return detect_weight(scale) > threshold


def object_not_placed(scale: Scale, threshold: float):
    print(detect_weight(scale))
    return detect_weight(scale) < threshold


def await_obj_state(detector: ObjectDetector, state: str, scale: Scale, threshold: float) -> None:
    states_dict = {"no_obj": [0, object_not_placed], "obj": [1, object_placed]}

    # detections_left = n_of_led_detections
    # while detections_left > 0:
    #     if detector.read_input() == states_dict[state][0]:
    #         detections_left -= 1
    
    detections_left = n_of_scale_detections
    while detections_left > 0:
        if states_dict[state][1](scale, threshold):
            detections_left -= 1


def await_obj_detection(detector: ObjectDetector, scale: Scale, threshold: float) -> None:
    print("waiting for obj detection")
    await_obj_state(detector, "obj", scale, threshold)
    print("detection done")


def await_no_obj_detection(detector: ObjectDetector, scale: Scale, threshold: float) -> None:
    await_obj_state(detector, "no_obj", scale, threshold)
