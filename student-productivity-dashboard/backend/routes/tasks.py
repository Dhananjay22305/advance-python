from fastapi import APIRouter, Depends, HTTPException
from typing import List
import schemas
import models

# 1. Create the Router (The Power Strip)
router = APIRouter()

# 2. Dependency (Local to this module for now)
def get_db():
    return models.tasks_db

# 3. Endpoints (Plugged into the Router, not the App)

# GET all tasks
@router.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: List = Depends(get_db)):
    return db

# CREATE a new task
@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: List = Depends(get_db)):
    new_id = len(db) + 1
    new_task_entry = models.Task(id=new_id, title=task.title)
    db.append(new_task_entry)
    return new_task_entry

# UPDATE task
@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def mark_done(task_id: int, db: List = Depends(get_db)):
    for task in db:
        if task.id == task_id:
            task.done = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")