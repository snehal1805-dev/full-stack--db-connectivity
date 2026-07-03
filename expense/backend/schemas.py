from pydantic import BaseModel

class add_user(BaseModel):
    name: str
    email: str
    password: str

class add_expense(BaseModel):
    title: str
    amount: float
    category: str

class delete_expense(BaseModel):
    id: int

class delete_user(BaseModel):
    id: int

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str

    

    class Config:
        from_attributes = True