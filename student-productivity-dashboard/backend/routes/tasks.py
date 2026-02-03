
from fastapi import APIRouter, Depends, HTTPException
from typing import List
import schemas
import models
from datetime import datetime

router = APIRouter()

def get_db():
    return models.tasks_db

# GET all tasks
# Notice response_model is now APIResponse
@router.get("/tasks", response_model=schemas.APIResponse)
def get_tasks(db: List = Depends(get_db)):
    return {
        "success": True,
        "message": "Tasks fetched successfully",
        "data": db  # The list goes inside 'data'
    }

# CREATE a new task
@router.post("/tasks", response_model=schemas.APIResponse)
def create_task(task: schemas.TaskCreate, db: List = Depends(get_db)):
    new_id = len(db) + 1
    new_task = models.Task(id=new_id, title=task.title) # created_at is auto
    db.append(new_task)
    
    return {
        "success": True,
        "message": "Task created successfully",
        "data": new_task # The single task goes inside 'data'
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": "Internal server error"}
    )

