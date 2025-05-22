from src.services.training_service import TrainingService
from src.models.exercise import Exercise
from src.strategy.cardio_strategy import CardioStrategy

import pytest

@pytest.fixture
def service():
    return TrainingService()

def test_create_workout(service):
    service.create_workout("Кардіо", "2024-05-22", CardioStrategy())
    workouts = service.get_workouts()
    assert len(workouts) == 1

def test_add_exercise_to_workout(service):
    service.create_workout("Сила", "2024-05-22", CardioStrategy())
    service.add_exercise_to_workout(0, "Присідання", 10, 80)
    workout = service.get_workout(0)
    assert len(workout.exercises) == 1

def test_total_calories(service):
    service.create_workout("Ранок", "2024-05-22", CardioStrategy())
    service.add_exercise_to_workout(0, "Біг", 15, 0)
    service.add_exercise_to_workout(0, "Стрибки", 5, 0)
    assert service.total_calories() == 170.0

def test_load_from_dict(service):
    data = [
        {
            "name": "Йога",
            "date": "2024-05-20",
            "exercises": [
                {"name": "Дихання", "duration": 5, "calories": 20}
            ]
        }
    ]
    service.load_from_dict(data, CardioStrategy())
    workouts = service.get_workouts()
    assert len(workouts) == 1

def test_to_dict_list(service):
    service.create_workout("Плавання", "2024-05-19", CardioStrategy())
    service.add_exercise_to_workout(0, "Кроль", 30, 0)
    dict_list = service.to_dict_list()
    assert isinstance(dict_list, list)
