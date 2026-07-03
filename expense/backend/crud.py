import models
import schemas
from sqlalchemy.orm import Session



def get_expense(db: Session, expense_id: int):
    return db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

def get_expenses(db: Session):
    return db.query(models.Expense).all()

def add_expense(db: Session, expense: schemas.add_expense):
    db_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()

    if db_expense:
        db.delete(db_expense)
        db.commit()
    return db_expense


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()

def get_users(db: Session):
    return db.query(models.User).all()

def add_user(db: Session, user: schemas.add_user):
    db_user = models.User(
        username=user.name,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user



