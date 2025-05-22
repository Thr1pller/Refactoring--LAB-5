from .base_strategy import TrainingStrategy

class StrengthStrategy(TrainingStrategy):
    def calculate_calories(self, sets: int, weight: float) -> float:
        return sets * weight * 0.3  # коефіцієнт для силового тренування
