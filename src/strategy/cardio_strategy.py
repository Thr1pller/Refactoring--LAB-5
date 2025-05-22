from .base_strategy import TrainingStrategy

class CardioStrategy(TrainingStrategy):
    def calculate_calories(self, duration_minutes: int) -> float:
        return duration_minutes * 8.5  # умовний коефіцієнт для кардіо
