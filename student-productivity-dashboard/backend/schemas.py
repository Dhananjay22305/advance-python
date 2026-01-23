# schemas.py
from pydantic import BaseModel

# Base schema with shared attributes
class TaskBase(BaseModel):
    title: str

# Schema for receiving data (User only sends title)
class TaskCreate(TaskBase):
    pass

# Schema for returning data (We add id and done status)
class TaskResponse(TaskBase):
    id: int
    done: bool