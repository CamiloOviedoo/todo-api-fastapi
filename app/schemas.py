from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str

class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    user_id: int