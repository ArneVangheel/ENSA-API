from pydantic import BaseModel


class CodesBase(BaseModel):
    code: str
    uses: int

class CodesEdit(BaseModel):
    uses: int

class CodesCreate(CodesBase):
    pass


class Codes(CodesBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True