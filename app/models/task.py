from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    title = db.Column(db.String(255), nullable=False)  # Заголовок задачи
    description = db.Column(db.Text, nullable=True)  # Описание
    status = db.Column(db.String(50), default="pending")  # Статус ("pending", "done")
