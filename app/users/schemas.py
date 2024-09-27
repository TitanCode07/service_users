from pydantic import BaseModel

class BaseUser(BaseModel):
    username: str
    email: str
    is_active: bool = True


class CreateUser(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        from_attributes = True