# app/models/user.py

from pydantic import BaseModel, EmailStr
from uuid import UUID


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    uuid: UUID
