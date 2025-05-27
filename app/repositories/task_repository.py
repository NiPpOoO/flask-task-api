class TaskRepository:
    @staticmethod
    def get_all():
        return Task.query.all()  # Получить все задачи

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)  # Найти задачу по ID

    @staticmethod
    def create(title, description):
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task
