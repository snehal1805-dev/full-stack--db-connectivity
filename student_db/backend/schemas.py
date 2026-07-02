
from pydantic import BaseModel

# Schema for creating student
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str


# Schema for updating student
class StudentUpdate(BaseModel):
    name: str
    age: int
    email: str


# Schema for returning student data
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True
