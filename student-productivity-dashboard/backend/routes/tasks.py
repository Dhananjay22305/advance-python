# routes/tasks.py
import logging  # <--- Import logging
from fastapi import APIRouter, Depends, HTTPException
from typing import List
import schemas
import models

router = APIRouter()

# 2. Create a "Logger" for this specific file
logger = logging.getLogger(__name__)

# Fake DB helper
def get_db():
    return models.tasks_db

@router.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: List = Depends(get_db)):
    # Log that someone asked for tasks
    logger.info("Fetching all tasks...") 
    return db

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: List = Depends(get_db)):
    new_id = len(db) + 1
    new_task_entry = models.Task(id=new_id, title=task.title)
    db.append(new_task_entry)
    
    # Log the action with data
    logger.info(f"New task created: ID {new_id} - Title: {task.title}")
    
    return new_task_entry

@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def mark_done(task_id: int, db: List = Depends(get_db)):
    for task in db:
        if task.id == task_id:
            task.done = True
            logger.info(f"Task {task_id} marked as DONE") # <--- Log success
            return task
            
    # Log the failure before crashing
    logger.error(f"User tried to update non-existent task: {task_id}")
    raise HTTPException(status_code=404, detail="Task not found")
