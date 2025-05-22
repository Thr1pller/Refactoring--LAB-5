import sys
import os
import pytest
from src.models.exercise import Exercise
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_exercise_creation():
    ex = Exercise("Присідання", 10, 80)
    assert ex.name == "Присідання"
    assert ex.duration == 10
    assert ex.calories == 80

def test_exercise_to_dict():
    ex = Exercise("Біг", 30, 250)
    data = ex.to_dict()
    assert data == {"name": "Біг", "duration": 30, "calories": 250}

def test_exercise_from_dict():
    data = {"name": "Планка", "duration": 5, "calories": 40}
    ex = Exercise.from_dict(data)
    assert ex.name == "Планка"
    assert ex.duration == 5
    assert ex.calories == 40

def test_exercise_str():
    ex = Exercise("Стрибки", 7, 60)
    assert str(ex) == "Стрибки - 7 хв - 60 ккал"
