
from pydantic import BaseModel
from datetime import datetime 

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    done: bool
    created_at: datetime 
