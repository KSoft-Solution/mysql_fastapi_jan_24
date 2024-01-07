from passlib.context import CryptContext
from datetime import datetime
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password):
    return pwd_context.hash(password)

def verify(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def create_customised_datetime():
    today = datetime.now()
    date_time = today.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time