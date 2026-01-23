# models.py

# This class mimics a Database Table entry
class Task:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        self.done = False

# This simulates our Database
tasks_db = []