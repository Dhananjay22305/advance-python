# main.py
from fastapi import FastAPI, HTTPException, Depends # <--- 1. Import Depends
from typing import List

import schemas
import models

app = FastAPI()

# --- THE DEPENDENCY (The Helper) ---
# Instead of a complex database connection, this simple function
# just returns your list.
def get_db():
    return models.tasks_db

@app.get("/", tags=["Root"])
def home():
    return {"message": "Backend is running"}

# --- THE ENDPOINTS (The Workers) ---

# GET all tasks
@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: List = Depends(get_db)): # <--- 2. Inject dependency
    # We use 'db' here, not 'models.tasks_db'
    return db

# CREATE a new task
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: List = Depends(get_db)):
    # Use 'db' to find the length
    new_id = len(db) + 1
    
    new_task_entry = models.Task(id=new_id, title=task.title)
    
    # Use 'db' to append
    db.append(new_task_entry)
    
    return new_task_entry

# UPDATE task
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def mark_done(task_id: int, db: List = Depends(get_db)):
    # Iterate through 'db' instead of the global variable
    for task in db:
        if task.id == task_id:
            task.done = True
            return task
    
    raise HTTPException(status_code=404, detail="Task not found")
