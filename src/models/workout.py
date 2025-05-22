from src.models.exercise import Exercise
from src.strategy.base_strategy import TrainingStrategy

class Workout:
    def __init__(self, name: str, date: str, strategy: TrainingStrategy):
        self.name = name
        self.date = date
        self.strategy = strategy
        self.exercises = []

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def total_calories(self):
        total = 0
        for ex in self.exercises:
            # Передаємо тільки те, що потрібно для обчислення
            if hasattr(self.strategy, "calculate_calories"):
                total += self.strategy.calculate_calories(
                    duration_minutes=ex.duration
                )
        return total

    def __str__(self):
        return f"{self.name} ({self.date}) - {len(self.exercises)} вправ"

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "exercises": [ex.to_dict() for ex in self.exercises],
            "strategy": self.strategy.__class__.__name__  # зберігаємо назву
        }

    @staticmethod
    def from_dict(data: dict, strategy: TrainingStrategy):
        workout = Workout(name=data.get("name", ""), date=data.get("date", ""), strategy=strategy)
        exercises = data.get("exercises", [])
        for ex in exercises:
            workout.add_exercise(Exercise.from_dict(ex))
        return workout
