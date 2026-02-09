from fastapi import APIRouter,Depends,HTTPException,status,Path
import models
from models import Users,Tasks
from sqlalchemy.orm import session
from database import Base,engine,SessionLocal
from typing import Annotated
from pydantics.taskrequest import TaskRequest
from .auth import get_current_user


router=APIRouter(prefix="/admin",tags=['Admin -Only accessible to admin users'])

def get_db():
    db=SessionLocal()#open connection
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]


@router.get('/tasks',status_code=status.HTTP_200_OK)
async def get_all_tasks(user:user_dependency,db:db_dependency):
    if user is None or user.get('user_role')!='admin':
        raise HTTPException(status_code=401,detail='Authentication failed')
    tasks=db.query(Tasks).all()
    return tasks

@router.delete('/deletetask/{taskid}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(user:user_dependency,db:db_dependency,taskid:int=Path(gt=0)):
    if user is None or user.get('user_role')!='admin':
        raise HTTPException(status_code=401,detail='Authentication failed')  
    task=db.query(Tasks).filter(Tasks.id==taskid).first()
    if task is None:
        raise HTTPException(status_code=404,detail='task  is not found')
    db.query(Tasks).filter(Tasks.id==taskid).delete()
    db.commit()