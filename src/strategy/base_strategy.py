from abc import ABC, abstractmethod

class TrainingStrategy(ABC):
    @abstractmethod
    def calculate_calories(self, **kwargs) -> float:
        pass
