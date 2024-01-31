
from fastapi import FastAPI
import uvicorn

from permited_sites import SOURCE_SITES
from dotenv import load_dotenv
from typing import Union

import models.incoming as incoming
import models.outgoing as outgoing
import utils as utils

app = FastAPI()
load_dotenv()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.post("/register")
async def register(payload: incoming.CreateUserPayload) -> Union[outgoing.CreateUserResponse, outgoing.DefaultResponse]:
    service = utils.import_class_from_file(SOURCE_SITES[payload.source_site], "SourceService")
    return getattr(service(), "register_user")(payload=payload)
    

@app.post("/users")
async def user_list(payload: incoming.UsersPayload) -> Union[outgoing.UsersList, outgoing.DefaultResponse]:
    service = utils.import_class_from_file(SOURCE_SITES[payload.source_site], "SourceService")
    return getattr(service(), "get_users")(payload=payload)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)