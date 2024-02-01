from pydantic import BaseModel
from typing import Optional

class CreateUserResponse(BaseModel):
    status: bool
    id: Optional[int] = None
    full_name: str
    email: str

class AuthorizedUser(BaseModel):
    id: int
    full_name: str
    email: str
    authorized: bool = False
    is_admin: bool = False

class UsersList(BaseModel):
    status: bool
    users: list[AuthorizedUser]

class UserDelete(BaseModel):
    status: bool

class DefaultResponse(BaseModel):
    status: bool
    msg: str