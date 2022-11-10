from object_detection.led_sensor import ObjectDetector
from object_detection.scale import Scale


n_of_detections = 10


def init_led_sensor(sensor_pin: int=17) -> ObjectDetector:
    detector = ObjectDetector(sensor_pin)
    print("Led sensor module initialized")
    return detector


def init_scale(sck: int = 5, dt: int = 6) -> Scale:
    scale = Scale(sck, dt)
    print("Scale module initialized")
    return scale


def detect_weight(scale: Scale) -> int:
    return scale.read_input()


def object_placed(scale: Scale, threshold: int):
    return detect_weight(scale) > threshold


def object_not_placed(scale: Scale, threshold: int):
    return detect_weight(scale) < threshold


def await_obj_state(detector: ObjectDetector, state: str, scale: Scale, threshold: int) -> None:
    states_dict = {"no_obj": [0, object_placed], "obj": [1, object_not_placed]}


    detections_left = n_of_detections
    while detections_left > 0:
        if detector.read_input() == states_dict[state][0]:
            detections_left -= 1
    
    while states_dict[state][1](scale, threshold):
        pass


def await_obj_detection(detector: ObjectDetector, scale: Scale, threshold: int) -> None:
    await_obj_state(detector, "obj", scale, threshold)


def await_no_obj_detection(detector: ObjectDetector, scale: Scale, threshold: int) -> None:
    await_obj_state(detector, "no_obj", scale, threshold)
