from typing import Dict
from sqlalchemy.orm import Session
from ..models.user import create_user, singleUser, update_user
from ..schemas.user import User
from ..utils.auth import hash

def register_new(user: User, db: Session):
    
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    return create_user(user=user, db=db)


def single_user(id: int, db: Session):
    return singleUser(db, id)
 

def updateUser(id:int, user:User, db: Session, values: Dict={}):
    return update_user(db=db, user=user, id=id, values=values)