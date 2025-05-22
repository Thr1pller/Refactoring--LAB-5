import json
from datetime import datetime

# Список тренувань (глобальний)
workouts = []

# Введення тренування вручну
def create_workout():
    name = input("Введіть назву тренування: ")
    date = input("Введіть дату (YYYY-MM-DD): ")
    workout = {
        "name": name,
        "date": date,
        "exercises": []
    }
    workouts.append(workout)
    print(f"Додано тренування: {name} ({date})")

# Додавання вправи до тренування
def add_exercise():
    if not workouts:
        print("Немає тренувань.")
        return
    show_workouts()
    index = int(input("Оберіть номер тренування: ")) - 1
    ex_name = input("Назва вправи: ")
    duration = int(input("Тривалість (хв): "))
    calories = int(input("Калорії: "))
    exercise = {
        "name": ex_name,
        "duration": duration,
        "calories": calories
    }
    workouts[index]["exercises"].append(exercise)
    print("Вправа додана.")

# Показати всі тренування
def show_workouts():
    if not workouts:
        print("Список порожній.")
        return
    for i, w in enumerate(workouts):
        print(f"{i + 1}. {w['name']} - {w['date']} ({len(w['exercises'])} вправ)")

# Показати вправи конкретного тренування
def show_exercises():
    if not workouts:
        print("Немає тренувань.")
        return
    show_workouts()
    index = int(input("Оберіть номер тренування: ")) - 1
    workout = workouts[index]
    print(f"Вправи для {workout['name']}:")
    for i, ex in enumerate(workout['exercises']):
        print(f"{i + 1}. {ex['name']} - {ex['duration']} хв - {ex['calories']} ккал")

# Підрахунок сумарних калорій
def total_calories():
    total = 0
    for workout in workouts:
        for ex in workout["exercises"]:
            total += ex["calories"]
    print(f"Всього спалено: {total} ккал")

# Збереження у файл
def save_to_file():
    with open("workouts.json", "w") as f:
        json.dump(workouts, f)
    print("Збережено у workouts.json")

# Завантаження з файлу
def load_from_file():
    global workouts
    try:
        with open("workouts.json", "r") as f:
            workouts = json.load(f)
        print("Завантажено успішно.")
    except FileNotFoundError:
        print("Файл не знайдено.")

# Меню
def main_menu():
    while True:
        print("\n===== Меню тренувань =====")
        print("1. Створити тренування")
        print("2. Додати вправу")
        print("3. Переглянути тренування")
        print("4. Переглянути вправи")
        print("5. Порахувати калорії")
        print("6. Зберегти")
        print("7. Завантажити")
        print("0. Вихід")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            create_workout()
        elif choice == "2":
            add_exercise()
        elif choice == "3":
            show_workouts()
        elif choice == "4":
            show_exercises()
        elif choice == "5":
            total_calories()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "0":
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main_menu()
