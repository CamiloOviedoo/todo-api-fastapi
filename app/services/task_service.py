from app.models import Task

def create_task_service(task, db):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks_service(db):
    return db.query(Task).all() 