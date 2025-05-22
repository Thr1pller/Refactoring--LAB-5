from src.services.training_service import TrainingService
from src.utils.io import save_json, load_json

def print_menu():
    print("\n===== Меню тренувань =====")
    print("1. Створити тренування")
    print("2. Додати вправу")
    print("3. Переглянути тренування")
    print("4. Переглянути вправи")
    print("5. Порахувати калорії")
    print("6. Зберегти")
    print("7. Завантажити")
    print("0. Вихід")

def main():
    service = TrainingService()
    filepath = "workouts.json"

    while True:
        print_menu()
        choice = input("Оберіть опцію: ")

        if choice == "1":
            name = input("Назва тренування: ")
            date = input("Дата (YYYY-MM-DD): ")
            service.create_workout(name, date)
            print("Тренування створено.")

        elif choice == "2":
            workouts = service.get_workouts()
            if not workouts:
                print("Немає тренувань.")
                continue
            for i, w in enumerate(workouts):
                print(f"{i + 1}. {w}")
            try:
                idx = int(input("Оберіть номер тренування: ")) - 1
                ex_name = input("Назва вправи: ")
                duration = int(input("Тривалість (хв): "))
                calories = int(input("Калорії: "))
                service.add_exercise_to_workout(idx, ex_name, duration, calories)
                print("Вправа додана.")
            except (ValueError, IndexError):
                print("Помилка вводу або індекс недійсний.")

        elif choice == "3":
            workouts = service.get_workouts()
            if not workouts:
                print("Список порожній.")
            else:
                for i, w in enumerate(workouts):
                    print(f"{i + 1}. {w}")

        elif choice == "4":
            workouts = service.get_workouts()
            if not workouts:
                print("Немає тренувань.")
                continue
            for i, w in enumerate(workouts):
                print(f"{i + 1}. {w.name}")
            try:
                idx = int(input("Оберіть номер тренування: ")) - 1
                workout = service.get_workout(idx)
                for i, ex in enumerate(workout.exercises):
                    print(f"{i + 1}. {ex}")
            except (ValueError, IndexError):
                print("Невірний номер.")

        elif choice == "5":
            print(f"Всього спалено: {service.total_calories()} ккал")

        elif choice == "6":
            save_json(filepath, service.to_dict_list())
            print("Дані збережено.")

        elif choice == "7":
            data = load_json(filepath)
            service.load_from_dict(data)
            print("Дані завантажено.")

        elif choice == "0":
            break

        else:
            print("Невірна опція.")

if __name__ == "__main__":
    main()
