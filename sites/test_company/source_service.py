
import models.incoming as incoming
import models.outgoing as outgoing
import os
from typing import Union
from sites.base_source_service import BaseSourceService

class SourceService(BaseSourceService):
    def register_user(self, payload: incoming.CreateUserPayload) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
        return outgoing.CreateUserResponse(status=True, full_name=payload.full_name, email=payload.email)


