# Flask Task API 🚀

Этот проект представляет собой **REST API** для управления задачами, созданный на Python (Flask) и PostgreSQL.

## 📌 Описание
API позволяет создавать, изменять, удалять и получать задачи, используя HTTP-запросы.

## 🔧 Установка
1. Клонируйте репозиторий:
git clone https://github.com/denis/flask-task-api.git

2. Перейдите в директорию проекта:
cd flask-task-api

3. Создайте виртуальное окружение:
python -m venv venv

4. Активируйте виртуальное окружение:
source venv/bin/activate # macOS/Linux venv\Scripts\activate # Windows

5. Установите зависимости:
pip install -r requirements.txt


## 🚀 Запуск проекта
1. Настройте `.env` файл с параметрами БД:
DATABASE_URL=postgresql://user:password@localhost/dbname

2. Запустите сервер:
flask run


## 📌 API-эндпоинты
| Метод | URL         | Описание              |
|-------|------------|-----------------------|
| GET   | /tasks     | Получить все задачи   |
| POST  | /tasks     | Создать новую задачу  |
| DELETE| /tasks/:id | Удалить задачу по ID  |

---

