from src.models.workout import Workout
from src.models.exercise import Exercise

class TrainingService:
    def __init__(self):
        self.workouts = []

    def create_workout(self, name: str, date: str):
        workout = Workout(name, date)
        self.workouts.append(workout)

    def add_exercise_to_workout(self, workout_index: int, name: str, duration: int, calories: int):
        if 0 <= workout_index < len(self.workouts):
            exercise = Exercise(name, duration, calories)
            self.workouts[workout_index].add_exercise(exercise)
        else:
            raise IndexError("Невірний індекс тренування")

    def get_workouts(self):
        return self.workouts

    def get_workout(self, index: int):
        if 0 <= index < len(self.workouts):
            return self.workouts[index]
        else:
            raise IndexError("Невірний індекс тренування")

    def total_calories(self):
        return sum(workout.total_calories() for workout in self.workouts)

    def load_from_dict(self, data_list: list):
        self.workouts.clear()
        for data in data_list:
            workout = Workout.from_dict(data)
            self.workouts.append(workout)

    def to_dict_list(self):
        return [workout.to_dict() for workout in self.workouts]
