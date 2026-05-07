from fastapi import HTTPException
from app.models import User

def create_user_service(user, db):
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username ya existe")
    
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
