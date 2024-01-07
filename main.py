import uvicorn;
from fastapi import FastAPI,Request,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.security import OAuth2PasswordBearer 

from app.config.database import Base,engine
from app.routes import user

app = FastAPI(title="SQL class 2024", version="0.1.1",
              description=" SQL class 2024 created with FastAPI and jwt Authenticated")

Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"Hello Complainers!"}

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
async def catch_exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"details": str(e)}))

app.middleware('http')(catch_exception_middleware)    

app.include_router(user.router)
    
    
if __name__ == '__main__':
    uvicorn.run('main:app', port=7000, host='0.0.0.0', reload=True)