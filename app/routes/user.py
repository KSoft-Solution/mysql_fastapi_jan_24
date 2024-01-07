from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..controllers.user import register_new
from ..schemas.user import  UserOpt,  User

router = APIRouter( tags = ['Users'])

@router.post("/user/register", status_code=status.HTTP_201_CREATED, response_model=UserOpt)
async def register(user:User, db:Session = Depends(get_db)):
    return register_new(db=db, user=user)
