from src.models.workout import Workout
from src.models.exercise import Exercise
from src.strategy.cardio_strategy import CardioStrategy

def test_workout_creation():
    w = Workout("Ранкове", "2024-05-22", CardioStrategy())
    assert w.name == "Ранкове"
    assert w.date == "2024-05-22"
    assert w.exercises == []

def test_add_exercise():
    w = Workout("Тренування", "2024-05-22", CardioStrategy())
    ex = Exercise("Біг", 20, 200)
    w.add_exercise(ex)
    assert len(w.exercises) == 1
    assert w.exercises[0] == ex

def test_total_calories():
    w = Workout("Тренування", "2024-05-22", CardioStrategy())
    w.add_exercise(Exercise("Біг", 10, 0))
    w.add_exercise(Exercise("Присідання", 15, 0))
    assert w.total_calories() == (10 + 15) * 8.5

def test_workout_to_dict_and_from_dict():
    w = Workout("Йога", "2024-05-22", CardioStrategy())
    w.add_exercise(Exercise("Дихання", 5, 20))
    data = w.to_dict()
    w2 = Workout.from_dict(data, CardioStrategy())
    assert w2.name == "Йога"
    assert w2.date == "2024-05-22"
    assert len(w2.exercises) == 1
    assert w2.exercises[0].name == "Дихання"
