from pydantic import BaseModel
from typing import Optional

class CreateUserPayload(BaseModel):
    source_site: str
    full_name: str
    email: str
    email_confirm: str
    password: str
    password_confirm: str

class UsersPayload(BaseModel):
    source_site: str
    full_name: Optional[str] = None
    email: Optional[str] = None

class DeleteUserPayload(BaseModel):
    source_site: str
    user_id: int