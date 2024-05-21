# deleted_tasks.py

class DeletedTasks:
    def __init__(self):
        self.deleted_tasks = []

    def add_deleted_task(self, task):
        self.deleted_tasks.append(task)

    def get_deleted_tasks(self):
        return self.deleted_tasks

