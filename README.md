# 🌤️ Weather App — Мгновенная погода по городам

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="python-version"/>
  <img src="https://img.shields.io/badge/Django-5.x-brightgreen.svg" alt="django-version"/>
  <img src="https://img.shields.io/badge/PostgreSQL-17-blue.svg" alt="postgresql"/>
  <img src="https://img.shields.io/badge/Redis-7-red.svg" alt="redis"/>
  <img src="https://img.shields.io/badge/DRF-3.14-orange.svg" alt="drf"/>
</p>

> ⚡️ **Тестовое задание:** Современное Django-приложение для получения актуальной погоды по городам через SSR и API.

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/alkogenius21/weather-site.git
```

---

### 2. Запуск через Docker Compose

**Требования:**
- Docker >= 21

**Шаги:**
1. Создайте файл `.env` в корне проекта и заполните его по шаблону (для БД).
2. Перейдите в папку `weather_site`, создайте `.env` и заполните его для приложения.
3. Запустите контейнеры:
    ```bash
    sudo docker compose up -d --build
    ```
4. Приложение будет доступно по адресу вашей машины или `localhost`.
5. После запуска контейнеров восстановите базу данных через дамп (`db_initial/`) с помощью любого менеджера БД (например, DBeaver).

---

### 3. Локальный запуск (dev-server)

**Требования:**
- Python >= 3.12.0
- Poetry >= 1.8.0 (опционально)

**Шаги:**
1. В `weather_site` создайте `.env` и заполните его по шаблону.
2. Убедитесь, что внешние сервисы (Postgres и Redis) доступны.
3. Создайте папку `log` внутри проекта.
4. Создайте и активируйте виртуальное окружение:
    - Через Poetry:
        ```bash
        poetry shell
        ```
    - Через Python:
        ```bash
        python -m venv venv
        source venv/bin/activate  # Linux
        venv\Scripts\activate.bat # Windows
        ```
5. Установите зависимости:
    - pip:
        ```bash
        pip install -r requirements.txt
        ```
    - Poetry:
        ```bash
        poetry install
        ```
6. Примените миграции:
    ```bash
    python manage.py migrate
    ```
7. Запустите приложение:
    ```bash
    python manage.py runserver
    ```

---

## 🌐 Эндпоинты

### 1. SSR (Django Templates)
- По умолчанию открывается версия на шаблонах.
- Один запрос реализован через контекст шаблона.
- Второй — на базе JavaScript.

### 2. API (Django Rest Framework)
- Эндпоинты: `/api/v1/some_path/`
- Документация:
    - Схема: `/api/v1/schema/`
    - Swagger UI: `/api/v1/swagger/`
- Реализован 1 основной эндпоинт (по ТЗ).

---

## 🏗 Архитектура

Вся логика вынесена в отдельное Django-приложение `core`, где реализовано получение координат города и погоды по ним. На его базе построены представления для SSR и API.

---

## 🛠️ Инструменты и качество кода

- Форматирование и проверка PEP8 — [Ruff](https://docs.astral.sh/ruff/)
- Конфигурация — в `pyproject.toml`

---

## 👨‍💻 Автор

- Разработчик: [Обухов Николай Романович](https://t.me/a1kogenius)

---

> ⭐️ Присоединяйтесь, тестируйте и предлагайте улучшения!
