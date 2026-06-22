from sqlalchemy import Column, DateTime, Integer, String
from database import Base
from datetime import datetime

class TaskDB(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status= Column(String,default="pending")
    due_date= Column(DateTime)
    crew_id=Column(Integer,nullable=True)

class DrillDB(Base):
    __tablename__ = "drills"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    type= Column(String)
    status= Column(String,default="pending")
    scheduled_date= Column(DateTime)
    ship_id=Column(Integer,nullable=True)