from abc import ABC, abstractmethod
from typing import Any

class Algorithm(ABC):
    @abstractmethod
    def process(self, data):
        pass

class AlgorithmA(Algorithm):
    def process(self, data: Any) -> Any:
        print("Processing data with Algorithm A")
        return data

class AlgorithmB(Algorithm):
    def process(self, data: Any) -> Any:
        print("Processing data with Algorithm B")
        return data


class AlgorithmC(Algorithm):
    def process(self, data: Any) -> Any:
        print("Processing data with Algorithm C")
        return data

class ProcessingService:
    def __init__(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def set_algorithm(self, algorithm:Algorithm) -> None:
        self.algorithm = algorithm
    
    def process(self, data):
        return self.algorithm.process(data)