class Exercise:
    def __init__(self, name: str, duration: int, calories: int):
        self.name = name
        self.duration = duration  # тривалість у хвилинах
        self.calories = calories  # кількість спалених калорій

    def __str__(self):
        return f"{self.name} - {self.duration} хв - {self.calories} ккал"

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "calories": self.calories
        }

    @staticmethod
    def from_dict(data: dict):
        return Exercise(
            name=data.get("name", ""),
            duration=int(data.get("duration", 0)),
            calories=int(data.get("calories", 0))
        )
