from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum
from typing import Optional


class DrillsCreate(BaseModel):
    title:str
    type:str
    scheduled_date:datetime

class DrillStatus(str,Enum):
    pending ="pending"
    in_progress = "inprogress"
    completed = "completed"
    missed ="missed"

class Drills(BaseModel):
    title:str
    type:str
    id:int
    scheduled_date:datetime
    status :DrillStatus = DrillStatus.pending
    attendance: List[int]=[]
    ship_id:Optional[int]=None