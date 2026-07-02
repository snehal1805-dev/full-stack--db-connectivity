from sqlalchemy import Column, Integer, String
from database import Base

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task= Column(String(255), nullable=False)
    description = Column(String(255))
    status = Column(String(50), nullable=False, default="pending")