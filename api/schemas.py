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

