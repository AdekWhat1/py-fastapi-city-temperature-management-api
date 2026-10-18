# Weather & Cities Management API

Модульний веб-сервіс на **FastAPI** для керування списком міст та збереження їхньої поточної температури з використанням асинхронного **Open-Meteo API**

## 🛠 Технологічний стек

* **Python 3.10+**
* **FastAPI** — веб-фреймворк
* **SQLAlchemy** — ORM для роботи з SQLite
* **Pydantic v2** — валідація даних
* **HTTPX** — асинхронний HTTP-клієнт для запитів до погодного API
* **Uvicorn** — ASGI-сервер

---

## 📁 Структура проєкту

```text
.
├── database.py         # Підключення до SQLite та налаштування SessionLocal
├── models.py           # Моделі БД (City, Temperature)
├── main.py             # Точка входу, ініціалізація FastAPI та підключення роутерів
├── cities/             # Модуль керування містами
│   ├── crud.py
│   ├── router.py
│   └── schemas.py
├── temperatures/       # Модуль керування температурами
│   ├── crud.py
│   ├── router.py
│   ├── schemas.py
│   └── service.py      # Асинхронний сервіс (httpx -> Open-Meteo API)
└── requirements.txt

🚀 Запуск проєкту
1. Клонування та створення віртуального середовища
Bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для Linux/macOS:
source venv/bin/activate
2. Встановлення залежностей
Bash
pip install -r requirements.txt
3. Запуск сервера Uvicorn
Bash
uvicorn main:app --reload
Після запуску сервіс буде доступний за адресою: http://127.0.0.1:8000

📖 Документація API
Інтерактивна документація (Swagger UI) генерується автоматично за адресою:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📌 Основні ендпоінти
Міста (/cities)
POST /cities/ — Додати нове місто

GET /cities/ — Отримати список міст

GET /cities/{city_id} — Отримати деталі міста

PUT /cities/{city_id} — Оновити дані міста

DELETE /cities/{city_id} — Видалити місто (з каскадним видаленням температур)

Температури (/temperatures)
POST /temperatures/?city_id={id} — Запитувати асинхронно поточну температуру для міста через Open-Meteo та зберегти запис у базі

GET /temperatures/ або GET /temperatures/?city_id={id} — Отримати історію температур (для всіх міст або з фільтром по city_id)


---

Запускайте проєкт командою `uvicorn main:app --reload` та відкривайте `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` для тестування всього CRUD-циклу