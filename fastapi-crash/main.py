from database import engine, Base, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
from schemas.maintenance import MaintenanceTaskCreate,TaskStatus
from schemas.drills import DrillsCreate,  DrillStatus
from typing import List
from datetime import datetime
from models import TaskDB
from models import DrillDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(engine)

@app.get("/")
def root():
    return{"message":"welcome"}
 
@app.post("/maintenance/admin/create")
def create_task(task: MaintenanceTaskCreate ,db:Session = Depends(get_db)):
  
    new_task = TaskDB(title=task.title,description=task.description,due_date=task.due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
@app.get("/maintenance/admin/all")
def get_all_tasks(db:Session = Depends(get_db)):
    db_tasks = db.query(TaskDB).all()
    return db_tasks


@app.put("/maintenance/admin/{id}/assign")
def assign_task(id: int, crew_id: int ,db:Session= Depends(get_db)):
    db_task = db.query(TaskDB).filter(TaskDB.id==id).first( )
    if db_task:
        db_task.crew_id=crew_id
        db.commit()
        db.refresh(db_task)
        return db_task
    return {"error": "Task not found"}


@app.put("/maintenance/admin/{id}/status")
def update_task(id: int, status:TaskStatus,db:Session = Depends(get_db)):
    db_uptask = db.query(TaskDB).filter(TaskDB.id==id).first()
    if db_uptask:
        db_uptask.status = status
        db.commit()
        db.refresh(db_uptask)
        return db_uptask
    return{ "error": "Tasknot found"}


@app.get("/maintenance/crew/{crew_id}/tasks")
def view_task(crew_id:int, db:Session =  Depends(get_db)):
     return db.query(TaskDB).filter(TaskDB.crew_id==crew_id).all()
   

    
@app.put("/maintenance/crew/{id}/status")
def crew_update_status(id: int, status:TaskStatus,db:Session =  Depends(get_db)):
    db_cupstatus = db.query(TaskDB).filter(TaskDB.id==id).first()
    if db_cupstatus:
        db_cupstatus.status = status
        db.commit()
        db.refresh(db_cupstatus)
        return db_cupstatus
    return{ "error": "Tasknot found"}

@app.post("/maintenance/crew/{id}/notes")
def notes(id: int, notes: str,db:Session =  Depends(get_db)):
    db_notes = db.query(TaskDB).filter(TaskDB.id==id).first()
    if db_notes:
        db_notes.notes = (db_notes.notes or []) + [notes]
        db.commit()
        db.refresh(db_notes)
        return db_notes
    return None

@app.post("/drills/admin/schedule")
def safety_drills(drill: DrillsCreate,db:Session = Depends(get_db)):
  
    schedule_drills= DrillDB(title=drill.title,type=drill.type,scheduled_date=drill.scheduled_date)
    db.add(schedule_drills)
    db.commit()
    db.refresh(schedule_drills)
    return schedule_drills

@app.put("/drills/admin/{id}/assign")
def assign_drill(id: int, ship_id: int,db:Session = Depends(get_db)):
    db_drill = db.query(DrillDB).filter(DrillDB.id==id).first( )
    if db_drill:
        db_drill.ship_id=ship_id
        db.commit()
        db.refresh(db_drill)
        return db_drill
    return {"error": "Drills not found"}

@app.get("/drills/crew/{ship_id}/drills")
def view_drills(ship_id:int,db:Session = Depends(get_db)):
    return db.query(DrillDB).filter(DrillDB.ship_id==ship_id).all()
    
    
@app.put("/drills/admin/{id}/attendance")
def mark_attendance(id: int, attendance: List[int],db:Session = Depends(get_db)):
    db_markdrillat = db.query(DrillDB).filter(DrillDB.id==id).first( )
    if db_markdrillat:
        db_markdrillat.attendance = attendance
        db.commit()
        db.refresh(db_markdrillat)
        return db_markdrillat 
    return {"error": "drill not found"}



@app.put("/drills/crew/{id}/status")
def mark_drill_status(id: int, status:DrillStatus,db:Session = Depends(get_db)):
    db_markdrillst = db.query(DrillDB).filter(DrillDB.id==id).first( )
    if db_markdrillst: 
        db_markdrillst.status = status
        db.commit()
        db.refresh(db_markdrillst)
        return db_markdrillst 
    return{ "error": "drill not  found"}

@app.get("/compliance/dashboard")
def compliance_dashboard(db:Session = Depends(get_db)):
    all_tasks = db.query(TaskDB).all()
    all_drills = db.query(DrillDB).all()
    now = datetime.utcnow()
    
    pending_tasks = [t for t in all_tasks if t.status == "pending"]
    completed_count = sum(1 for t in all_tasks if t.status == "completed")
    pending_count = len(pending_tasks)
    overdue_tasks = [t for t in all_tasks if t.due_date and t.due_date < now and t.status != "completed"]
    missed_drills = [d for d in all_drills if d.scheduled_date and d.scheduled_date < now and d.status != "completed"]

   
    return {
        "pending_tasks": pending_tasks,
        "missed_drills": missed_drills,
        "overdue_maintenance": overdue_tasks,
        "completed_count": completed_count,
        "pending_count": pending_count
    }
    

