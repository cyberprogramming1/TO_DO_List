# task.py

class Task:
    def __init__(self, task_id, task_name, status):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status

    def __str__(self):
        return f"| {self.task_id:<6} | {self.task_name:<50} | {self.status:<10} |"
