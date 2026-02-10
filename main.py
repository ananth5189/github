from fastapi import FastAPI,Depends,HTTPException,status,Path
import models
from models import Users,Tasks
from sqlalchemy.orm import session
from database import Base,engine,SessionLocal
from typing import Annotated
from routers import auth,tasks,admin,user

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(tasks.router)

