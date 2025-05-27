from app.repositories.task_repository import TaskRepository

class TaskService:
    @staticmethod
    def get_all_tasks():
        tasks = TaskRepository.get_all()
        return [{"id": t.id, "title": t.title, "status": t.status} for t in tasks]

    @staticmethod
    def create_task(title, description):
        task = TaskRepository.create(title, description)
        return {"message": "Task created", "id": task.id}
