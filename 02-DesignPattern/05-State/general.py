from abc import ABC, abstractmethod

# 抽象状态
class TrafficLightState(ABC):

    @abstractmethod
    def next(self, context: "TrafficLight") -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass


# 红灯状态
class RedState(TrafficLightState):

    def next(self, context: "TrafficLight") -> None:
        print("RED -> GREEN")
        context.set_state(GreenState())

    def display(self) -> None:
        print("RED: Stop")


# 绿灯状态
class GreenState(TrafficLightState):

    def next(self, context: "TrafficLight") -> None:
        print("GREEN -> YELLOW")
        context.set_state(YellowState())

    def display(self) -> None:
        print("GREEN: Go")


# 黄灯状态
class YellowState(TrafficLightState):

    def next(self, context: "TrafficLight") -> None:
        print("YELLOW -> RED")
        context.set_state(RedState())

    def display(self) -> None:
        print("YELLOW: Slow down")

# Context/状态机本体
class TrafficLight:

    def __init__(self):
        self._current_state: TrafficLightState = RedState()

    def set_state(self, new_state: TrafficLightState) -> None:
        self._current_state = new_state

    def display(self) -> None:
        self._current_state.display()
    
    def next(self) -> None:
        self._current_state.next(self)

# Usage
light = TrafficLight()

for _ in range(6):
    light.display()
    light.next()