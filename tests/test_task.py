import unittest
from app.services.task_service import TaskService

class TaskTest(unittest.TestCase):
    def test_create_task(self):
        task = TaskService.create_task("New Task", "Test Description")
        self.assertEqual(task["message"], "Task created")

if __name__ == "__main__":
    unittest.main()
