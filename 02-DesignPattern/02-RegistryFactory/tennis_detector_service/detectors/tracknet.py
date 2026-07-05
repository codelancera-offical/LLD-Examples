# detectors/tracknet.py

from .base import Detector


class TrackNetDetector(Detector):
    def __init__(self, checkpoint: str, device: str = "cpu"):
        self.checkpoint = checkpoint
        self.device = device

    def detect(self, frame):
        print(f"TrackNet detecting on {self.device}")
        return []