# schemas.py
from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

# Your existing Task schemas
class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    done: bool
    created_at: datetime

# --- NEW: The Centralized Wrapper ---
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None # 'Any' means it can be a List or a Dict
