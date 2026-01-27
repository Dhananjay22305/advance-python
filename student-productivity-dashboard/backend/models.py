
from datetime import datetime # <--- 1. Import the clock tool

class Task:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        self.done = False
        self.created_at = datetime.now() 

# This simulates our Database
tasks_db = []
