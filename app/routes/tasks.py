from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import TaskCreate
from app.services import task_service

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task_service(task, db)

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks_service(db)
