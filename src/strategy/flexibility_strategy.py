from .base_strategy import TrainingStrategy

class FlexibilityStrategy(TrainingStrategy):
    def calculate_calories(self, duration_minutes: int) -> float:
        return duration_minutes * 4.0  # гнучкість - нижча інтенсивність
