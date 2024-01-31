
import models.incoming as incoming
import models.outgoing as outgoing
import os
from typing import Union

class BaseSourceService:
    def register_user(self, payload: incoming.CreateUserPayload) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
        error_message = self.validate_password(payload.password, payload.password_confirm)
        if error_message:
            return outgoing.DefaultResponse(status=False, msg=error_message)
        return outgoing.CreateUserResponse(status=True, full_name=payload.full_name, email=payload.email)

    def get_users(self, payload: incoming.UsersPayload) -> Union[outgoing.UsersList, outgoing.DefaultResponse]:
        return outgoing.UsersList(users=list())

    def validate_password(self, password, password_confirm):
        if password != password_confirm:
            return "Passwords do not match."
    
        if len(password) <= int(os.environ.get("MINIMAL_PASSWORD_LENGTH", '2')):
            return "Password is too short"


