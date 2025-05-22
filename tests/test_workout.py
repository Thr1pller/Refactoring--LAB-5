import sys
import os
import pytest
from src.models.workout import Workout
from src.models.exercise import Exercise
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_workout_creation():
    w = Workout("Ранкове", "2024-05-22")
    assert w.name == "Ранкове"
    assert w.date == "2024-05-22"
    assert w.exercises == []

def test_add_exercise():
    w = Workout("Тренування", "2024-05-22")
    ex = Exercise("Біг", 20, 200)
    w.add_exercise(ex)
    assert len(w.exercises) == 1
    assert w.exercises[0] == ex

def test_total_calories():
    w = Workout("Тренування", "2024-05-22")
    w.add_exercise(Exercise("Біг", 10, 100))
    w.add_exercise(Exercise("Присідання", 15, 80))
    assert w.total_calories() == 180

def test_workout_to_dict_and_from_dict():
    w = Workout("Йога", "2024-05-22")
    w.add_exercise(Exercise("Дихання", 5, 20))
    data = w.to_dict()
    w2 = Workout.from_dict(data)
    assert w2.name == "Йога"
    assert w2.date == "2024-05-22"
    assert len(w2.exercises) == 1
    assert w2.exercises[0].name == "Дихання"
