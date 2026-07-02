
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()



# Create Student
@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    db_student = models.Student(
        name=student.name,
        age=student.age,
        email=student.email
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


# Get Single Student
@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return db_student


# Get All Students
@app.get("/students/", response_model=list[schemas.StudentResponse])
def read_students(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    students = db.query(models.Student).offset(skip).limit(limit).all()

    return students


# Update Student
@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    # Check if student exists
    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update fields
    db_student.name = student.name
    db_student.age = student.age
    db_student.email = student.email

    # Save changes
    db.commit()
    db.refresh(db_student)

    return db_student
