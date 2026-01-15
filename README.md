# ML Inference API

Это мой учебный проект, в котором я реализовал ML inference сервис с использованием FastAPI и scikit-learn. 

## Что реализовано сейчас

- FastAPI приложение
- Загрузка модели один раз при старте сервиса _(через `lifespan`)_
- Dependecy Injection для доступа к модели в эндпоинтах
- Валидация входных данных с помощью Pydantic
- Эндпоинт для предсказания
- Healthcheck эндпоинт

## Структура проекта

```text
app/
├── main.py              # Точка входа приложения
├── api/
│   ├── routers/
│   │   ├── predict.py   # Endpoints для предсказаний
│   │   └── health.py    # Healthcheck
│   └── deps.py          # Dependency-функции
├── core/
│   └── lifespan.py      # Жизненный цикл приложения
├── ml/
│   ├── model.py         # Логика inference
│   └── train.py         # Обучение модели
├── schemas/
│   └── predict.py       # Pydantic-схемы
```

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/first_ml_api.git
   cd first_ml_api
    ```
2. Установите зависимости:
    ```bash
    python -m venv venv
    source venv/bin/activate # для Linux/Mac
    pip install -r requirements.txt
    ```
3. Обучение модели:
    ```bash
    python app/ml/train.py
    ```

4. Запустите приложение:
    ```bash
    uvicorn app.main:app --reload
    ```

Приложение будет доступно по адресу `http://127.0.0.1:8000`

## Будущие улучшения

- Обучить реальную модель, а не использовать заглушку
- Добавить preprocessing
- Добавить логирование запросов и ошибок
- Ну и еще чето крутое :)