
import models.incoming as incoming
import models.outgoing as outgoing
import os
from typing import Union
from sites.services import BaseSourceService
from sqlalchemy.orm import Session

class SourceService(BaseSourceService):
    def register_user(self, payload: incoming.CreateUserPayload, db: Session ) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
        return outgoing.CreateUserResponse(status=True, full_name=payload.full_name, email=payload.email)
