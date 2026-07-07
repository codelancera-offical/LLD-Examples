from abc import ABC, abstractmethod
import time

# Component, waiting to be decorated
class Detector(ABC):

    @abstractmethod
    def detect(self, video_path:str) ->dict:
        pass

class TrackNetV5Detector(Detector):

    def detect(self, video_path: str) -> dict:
        print(f"V5 detecting: {video_path}")

        return {
            "video_path": video_path,
            "ball_count": 128
        }
    
# Abstract Decorator
class DetectorDecorator(Detector):

    def __init__(self, inner:Detector):
        self._inner = inner

class ValidationDecorator(DetectorDecorator):

    def validate(self, video_path):
        if not video_path:
            raise ValueError("video_path can not be empty")
    
    def detect(self, video_path: str) -> dict:
        self.validate(video_path)

        print("validation pass")

        return self._inner.detect(video_path)
    
class TimingDecorator(DetectorDecorator):

    def detect(self, video_path: str) -> dict:
        start_time = time.perf_counter()

        result = self._inner.detect(video_path)

        elapsed_time = time.perf_counter() - start_time
        print(f"检测耗时：{elapsed_time:.4f} 秒")

        return result

if __name__ == "__main__":

    detector = TimingDecorator(
        ValidationDecorator(
            TrackNetV5Detector()
        )
    )

    result = detector.detect("match.mp4")

    print(result)