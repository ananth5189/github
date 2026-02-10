from pydantic import BaseModel,Field

class CreateUserRequest(BaseModel):
    username: str
    email: str
    firstname:str
    lastname:str
    password:str
    role:str