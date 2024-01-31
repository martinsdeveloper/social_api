from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    status: bool
    full_name: str
    email: str

class AuthorizedUser(BaseModel):
    status: bool
    full_name: str
    email: str
    authorized: bool
    is_admin: bool = False

class UsersList(BaseModel):
    users: list[AuthorizedUser]

class DefaultResponse(BaseModel):
    status: bool
    msg: str