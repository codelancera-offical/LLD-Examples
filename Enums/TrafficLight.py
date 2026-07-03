from enum import Enum

class TrafficLight(Enum):
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self) -> 'TrafficLight':
        if self == TrafficLight.RED:
            return TrafficLight.GREEN
        elif self == TrafficLight.GREEN:
            return TrafficLight.YELLOW
        elif self == TrafficLight.YELLOW:
            return TrafficLight.RED
    
    def display(self) -> None:
        print(f"{self.name} ({self.value} seconds)")


if __name__ == "__main__":
    current_light = TrafficLight.RED
    for _ in range(6):
        current_light.display()
        current_light = current_light.next()