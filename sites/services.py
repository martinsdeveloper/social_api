
import models.incoming as incoming
import models.outgoing as outgoing
import models.db as base

from sqlalchemy.orm import Session
from typing import Union

import os
import bcrypt

class BaseSourceService:
    def register_user(self, payload: incoming.CreateUserPayload, db: Session) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
        error_message = self.validate_password(payload.password, payload.password_confirm)
        if error_message:
            return outgoing.DefaultResponse(status=False, msg=error_message)
        user = UserService.save_user(payload=payload, db=db)
        return outgoing.CreateUserResponse(status=True, id=user.id, full_name=payload.full_name, email=payload.email)

    def get_users(self, payload: incoming.UsersPayload, db: Session) -> Union[outgoing.UsersList, outgoing.DefaultResponse]:
        return outgoing.UsersList(status=True, users=list(UserService.get_users(payload=payload, db=db)))

    def delete_user(self, payload: incoming.CreateUserPayload, db: Session) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
        user = UserService.delete_user(payload=payload, db=db)
        return outgoing.UserDelete(status=True)

    def validate_password(self, password, password_confirm):
        if password != password_confirm:
            return "Passwords do not match."
    
        if len(password) <= int(os.environ.get("MINIMAL_PASSWORD_LENGTH", '2')):
            return "Password is too short"


class UserService:
    @staticmethod
    def save_user(payload: incoming.CreateUserPayload, db: Session):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(payload.password.encode('utf-8'), salt)
        salt_str = salt.decode('utf-8')
        hashed_password_str = hashed_password.decode('utf-8')
        new_user = base.User(full_name=payload.full_name, email=payload.email, password=hashed_password_str, salt=salt_str)
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except Exception as e:
            print(f"Error adding user to the database: {e}")
            db.rollback()
        return new_user

    @staticmethod
    def get_users(db: Session, payload: incoming.UsersPayload):
        for usr in db.query(base.User).all():
            yield(outgoing.AuthorizedUser(id=usr.id, full_name=usr.full_name, email=usr.email, authorized=False, is_admin=False))

    @staticmethod
    def delete_user(db: Session, payload: incoming.DeleteUserPayload):
        try:
            user_to_delete = db.query(base.User).filter(base.User.id == payload.user_id).first()
            if user_to_delete:
                db.delete(user_to_delete)
                db.commit()
            else:
                raise Exception("User not found")
        except Exception as e:
            print(f"Error deleting user from the database: {e}")
            db.rollback()
            return outgoing.UserDelete(status=False)
        return outgoing.UserDelete(status=True)
