from pydantic import BaseModel
from datetime import datetime


class BaseScheme(BaseModel):
    text: str


class CommentCreate(BaseScheme):
    task_id: int


class CommentUpdate(CommentCreate):
    pass


class CommentResponse(BaseScheme):
    id: int
    task_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    username: str
    password: str


class RequestBody(BaseModel):
    comment: CommentCreate
    login_data: LoginData
