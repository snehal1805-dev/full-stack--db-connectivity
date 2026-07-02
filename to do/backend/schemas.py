from pydantic import BaseModel

class TodoCreate(BaseModel):
    task: str
    description: str
    status: str

class TodoUpdate(BaseModel):
    task: str
    description: str
    status: str

class TodoDelete(BaseModel):
    id: int

class TodoResponse(BaseModel):
    id: int
    task: str
    description: str
    status: str

    class Config:
        from_attributes = True
