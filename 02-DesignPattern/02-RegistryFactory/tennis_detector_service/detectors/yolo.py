# detectors/yolo.py

from .base import Detector


class YOLODetector(Detector):
    def __init__(self, model_path: str):
        self.model_path = model_path

    def detect(self, frame):
        print("YOLO detecting")
        return []