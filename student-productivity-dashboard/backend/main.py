# main.py
from fastapi import FastAPI, HTTPException
from typing import List

# Import our modular files
import schemas
import models

app = FastAPI()

@app.get("/", tags=["Root"])
def home():
    return {"message": "Backend is running"}

# GET all tasks
# response_model ensures we return a list of TaskResponse schemas
@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks():
    return models.tasks_db

# CREATE a new task
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate):
    # Generate a simple ID (in a real DB, this is automatic)
    new_id = len(models.tasks_db) + 1
    
    # Create the internal Model instance
    new_task_entry = models.Task(id=new_id, title=task.title)
    
    # Save to "DB"
    models.tasks_db.append(new_task_entry)
    
    return new_task_entry

# UPDATE task
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def mark_done(task_id: int):
    # Search for the task by ID
    # (In a real DB, this would be a query like db.get(id))
    for task in models.tasks_db:
        if task.id == task_id:
            task.done = True
            return task
    
    # If loop finishes without finding task, raise 404
    raise HTTPException(status_code=404, detail="Task not found")