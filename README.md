# 💪 Fitness Training Manager

Менеджер тренувань для фітнес-додатку, реалізований на Python з дотриманням принципів SOLID, впровадженням патерну Strategy, модульним тестуванням та аналізом коду через SonarQube.

## 🎯 Мета проєкту

Провести рефакторинг початкового неструктурованого Python-коду, впровадивши об’єктно-орієнтований підхід, шаблони проєктування, SOLID-принципи та покриття коду тестами з подальшим аналізом через SonarQube.

## 📝 Завдання

- Виявити порушення SOLID у `bad_main.py`.
- Провести поетапний рефакторинг із поділом на сутності.
- Впровадити шаблон проєктування **Strategy** для обчислення калорій.
- Реалізувати сервіси, утиліти, тести, структуру.
- Забезпечити модульне тестування (`pytest`) з покриттям (`coverage.xml`).
- Провести аналіз якості коду за допомогою **SonarQube**.

## 🔥 Унікальність проєкту

- **Тематика**: не банківська система чи ресторан — а **фітнес-трекер**.
- **Стратегії**: реалізовано окремі логіки для Cardio, Strength, Flexibility-тренувань.
- **Архітектура**: повністю авторська структура з рефакторингом через класи, сервіси, стратегії.
- **Гнучкість**: Workout працює через інтерфейс, підтримує зміну стратегії під час виконання.
- **Інтеграція**: GitHub, SonarQube, coverage, PEP8-стиль, автоматизація.

## 🔁 Принципи рефакторингу

- ✅ Розділення відповідальностей (SRP)
- ✅ Відкритість до розширення (OCP)
- ✅ Використання інтерфейсів (`TrainingStrategy`) — DIP
- ✅ Модульність, повторне використання
- ✅ Заміна логіки через шаблон Strategy без зміни ядра системи

## ✅ Виконане

- ✅ Реалізовано 3 стратегії (Cardio, Strength, Flexibility)
- ✅ Всі об'єкти: Workout, Exercise, TrainingService, Strategy
- ✅ Покриття тестами: понад 83%
- ✅ Пройдено аналіз SonarQube: оцінка `A` за всіма метриками
- ✅ Повна документація та структурування

## 📁 Структура проєкту

```
LAB5/
├── bad_main.py                      # Початковий код до рефакторингу
├── new_main.py                      # Відрефакторений інтерактивний інтерфейс
├── src/
│   ├── models/
│   │   ├── exercise.py
│   │   └── workout.py
│   ├── services/
│   │   └── training_service.py
│   ├── utils/
│   │   └── io.py
│   └── strategy/
│       ├── base_strategy.py
│       ├── cardio_strategy.py
│       ├── strength_strategy.py
│       └── flexibility_strategy.py
├── tests/
│   ├── test_exercise.py
│   ├── test_workout.py
│   ├── test_training_service.py
│   └── test_strategy.py
├── coverage.xml
├── pytest.ini
├── sonar-project.properties
└── README.md
```

## ⚙️ Інструкція для запуску

```bash
pip install pytest pytest-cov
pytest --cov=src --cov-report=xml
sonar-scanner
```

## 👤 Автор

Константінов Микита, ФЕП-32  
Лабораторна робота 5 — *«Аналіз та рефакторинг коду»*