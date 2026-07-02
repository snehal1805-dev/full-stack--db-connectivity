import models
import schemas
from sqlalchemy.orm import Session

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(
        models.ToDo.id == todo_id
    ).first()

def get_todos(db: Session):
    return db.query(models.Todo).all()  

def add_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.ToDo(
        task=todo.task,
        description=todo.description,
        status=todo.status
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.ToDo).filter(
        models.ToDo.id == todo_id
    ).first()

    if db_todo:
        db_todo.task = todo.task
        db_todo.description = todo.description
        db_todo.status = todo.status
        db.commit()
        db.refresh(db_todo)
    return db_todo  

def delete_todo(db: Session, todo_id: int): 
    db_todo = db.query(models.Todo).filter(
        models.ToDo.id == todo_id
    ).first()

    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo

