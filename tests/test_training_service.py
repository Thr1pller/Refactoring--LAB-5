import pytest
from src.services.training_service import TrainingService
from src.models.exercise import Exercise

@pytest.fixture
def service():
    return TrainingService()

def test_create_workout(service):
    service.create_workout("Кардіо", "2024-05-22")
    workouts = service.get_workouts()
    assert len(workouts) == 1
    assert workouts[0].name == "Кардіо"
    assert workouts[0].date == "2024-05-22"

def test_add_exercise_to_workout(service):
    service.create_workout("Сила", "2024-05-22")
    service.add_exercise_to_workout(0, "Присідання", 10, 80)
    workout = service.get_workout(0)
    assert len(workout.exercises) == 1
    assert workout.exercises[0].name == "Присідання"

def test_total_calories(service):
    service.create_workout("Ранок", "2024-05-22")
    service.add_exercise_to_workout(0, "Біг", 15, 120)
    service.add_exercise_to_workout(0, "Стрибки", 5, 50)
    assert service.total_calories() == 170

def test_get_workout_invalid_index(service):
    with pytest.raises(IndexError):
        service.get_workout(0)

def test_add_exercise_invalid_index(service):
    with pytest.raises(IndexError):
        service.add_exercise_to_workout(5, "Віджимання", 5, 30)

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
    service.load_from_dict(data)
    workouts = service.get_workouts()
    assert len(workouts) == 1
    assert workouts[0].name == "Йога"
    assert workouts[0].exercises[0].name == "Дихання"

def test_to_dict_list(service):
    service.create_workout("Плавання", "2024-05-19")
    service.add_exercise_to_workout(0, "Кроль", 30, 200)
    dict_list = service.to_dict_list()
    assert isinstance(dict_list, list)
    assert dict_list[0]["name"] == "Плавання"
    assert dict_list[0]["exercises"][0]["name"] == "Кроль"
