from pydantic import BaseModel
from typing import Optional
from enum import Enum
from typing import List
from datetime import datetime

class MaintenanceTaskCreate(BaseModel):
    title: str
    description: str
    due_date:datetime
    
class TaskStatus(str,Enum):
    pending = "pending"
    completed= "completed"
    in_progress = "in_progress"


class MaintenanceTask(BaseModel):
    title:str
    description:str
    id:int
    status: TaskStatus= TaskStatus.pending
    crew_id:Optional[int]=None
    due_date:Optional[datetime] = None

    notes: List[str] =[]


