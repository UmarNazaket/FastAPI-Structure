# app/db/models/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr
    hashed_password: str