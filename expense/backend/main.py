from database import get_db,engine, Base
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db)
    return expenses

@app.get("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = crud.get_expense(db, expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense

@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.add_expense, db: Session = Depends(get_db)):
    db_expense = crud.add_expense(db, expense)
    return db_expense

@app.delete("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = crud.delete_expense(db, expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense

@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.add_user, db: Session = Depends(get_db)):
    db_user = crud.add_user(db, user)
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/")
def root():
    return {"message": "Welcome to the Expense Tracker API!"}

