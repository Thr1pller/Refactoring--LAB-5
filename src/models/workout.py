from datetime import datetime
from src.models.exercise import Exercise

class Workout:
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date  # формат YYYY-MM-DD
        self.exercises = []

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def total_calories(self):
        return sum(ex.calories for ex in self.exercises)

    def __str__(self):
        return f"{self.name} ({self.date}) - {len(self.exercises)} вправ"

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "exercises": [ex.to_dict() for ex in self.exercises]
        }

    @staticmethod
    def from_dict(data: dict):
        workout = Workout(name=data.get("name", ""), date=data.get("date", ""))
        exercises = data.get("exercises", [])
        for ex in exercises:
            workout.add_exercise(Exercise.from_dict(ex))
        return workout
