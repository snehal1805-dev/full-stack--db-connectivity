from sqlalchemy.orm import Session

import models
import schemas


# Create Student
def create_student(db: Session, student: schemas.StudentCreate):
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
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()


# Get All Students
def get_students(db: Session):
    return db.query(models.Student).all()

