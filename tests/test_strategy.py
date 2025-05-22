import pytest
from src.strategy.cardio_strategy import CardioStrategy
from src.strategy.strength_strategy import StrengthStrategy
from src.strategy.flexibility_strategy import FlexibilityStrategy
from src.models.workout import Workout
from src.models.exercise import Exercise

def test_cardio_strategy():
    strategy = CardioStrategy()
    calories = strategy.calculate_calories(duration_minutes=30)
    assert calories == 255.0  # 30 * 8.5

def test_strength_strategy():
    strategy = StrengthStrategy()
    calories = strategy.calculate_calories(sets=5, weight=50)
    assert calories == 75.0  # 5 * 50 * 0.3

def test_flexibility_strategy():
    strategy = FlexibilityStrategy()
    calories = strategy.calculate_calories(duration_minutes=20)
    assert calories == 80.0  # 20 * 4.0

def test_workout_with_cardio_strategy():
    strategy = CardioStrategy()
    workout = Workout("Кардіо ранок", "2024-06-10", strategy)
    workout.add_exercise(Exercise("Біг", 30, 0))
    assert workout.total_calories() == 255.0

def test_workout_with_flexibility_strategy():
    strategy = FlexibilityStrategy()
    workout = Workout("Розтяжка", "2024-06-10", strategy)
    workout.add_exercise(Exercise("Йога", 15, 0))
    assert workout.total_calories() == 60.0

def test_strategy_switching_runtime():
    cardio = CardioStrategy()
    flex = FlexibilityStrategy()
    workout = Workout("Тест", "2024-06-10", cardio)
    workout.add_exercise(Exercise("Біг", 10, 0))
    assert workout.total_calories() == 85.0

    # Змінюємо стратегію
    workout.strategy = flex
    assert workout.total_calories() == 40.0  # 10 * 4.0
