from typing import Dict
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from ..config.database import  Base 
from ..schemas.user import CreateUser
from ..utils.auth import create_customised_datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(20), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    password = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
def create_user(user: CreateUser, db: Session,):
    newUser = User(username=user.username, email=user.email, password=user.password)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser


def singleUser(db: Session, id: int):
    
    query_user =  db.query(User).filter(User.id == id).first()
  
    return query_user


def update_user(db: Session,  user: User, id: int, values: Dict={}):
    values['updated_at'] = create_customised_datetime()
    updated = db.query(User).filter(User.id == id)
    
    updated.update(values)
    db.commit()
    
    return updated.first()