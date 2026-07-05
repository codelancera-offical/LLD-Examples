from detectors.base import Detector
from detectors.tracknet import TrackNetDetector
from detectors.yolo import YOLODetector


DETECTOR_REGISTRY: dict[str, type[Detector]] = {
    "tracknet": TrackNetDetector,
    "yolo": YOLODetector,
}


def create_detector(name: str, **kwargs) -> Detector:
    try:
        detector_class = DETECTOR_REGISTRY[name]
    except KeyError:
        available = ", ".join(DETECTOR_REGISTRY)
        raise ValueError(
            f"Unknown detector '{name}'. "
            f"Available: {available}"
        ) from None

    return detector_class(**kwargs)