from detector_factory import create_detector


class TennisPipeline:
    def __init__(self, detector_config: dict):
        config = detector_config.copy()
        detector_type = config.pop("type")

        self.detector = create_detector(
            detector_type,
            **config,
        )

    def run(self, frame):
        return self.detector.detect(frame)