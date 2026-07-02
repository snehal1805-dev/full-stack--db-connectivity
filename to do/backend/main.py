from fastapi import FastAPI , Depends, HTTPException

from database import engine, Base, get_db
from models import ToDo

from sqlalchemy.orm import Session


import schemas
import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/todos" ,response_model=list[schemas.TodoResponse])
def read_todo(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
    ):
    todos    = db.query(models.ToDo).offset(skip).limit(limit).all()

    return todos

@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, 
              db: Session = Depends(get_db)
              ):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.ToDo(
        task=todo.task,
        description=todo.description,
        status=todo.status
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db_todo.task = todo.task
    db_todo.description = todo.description
    db_todo.status = todo.status
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}", response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(db_todo)
    db.commit()
    return db_todo