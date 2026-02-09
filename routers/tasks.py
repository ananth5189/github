from fastapi import APIRouter,Depends,HTTPException,status,Path
import models
from models import Users,Tasks
from sqlalchemy.orm import session
from database import Base,engine,SessionLocal
from typing import Annotated
from pydantics.taskrequest import TaskRequest
from .auth import get_current_user


router=APIRouter(prefix="/tasks",tags=['Tasks Service'])


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]

# gives all data in todos table
@router.get('/',status_code=status.HTTP_200_OK)
async def get_all_tasks_of_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='User is unauthenticated! Please login')
    tasks=db.query(Tasks).filter(Tasks.owner_id==user.get('user_id')).all()
    return tasks

@router.get('/{task_id}',status_code=status.HTTP_200_OK)
async def get_task_by_id_and_userid(user:user_dependency,db:db_dependency,task_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='User is unauthenticated! Please login')
    todo= db.query(Tasks).filter(Tasks.id==task_id).filter(Tasks.owner_id==user.get('user_id')).first()
    if todo is not None:
        return todo
    return HTTPException(status_code=404,detail='task with id for the user is not found')


@router.post('/createtask/',status_code=status.HTTP_201_CREATED)
async def create_task(user:user_dependency,db:db_dependency,task:TaskRequest):
    if user is None:
        raise HTTPException(status_code=401,detail='Unauthenticated!!')
    newtask=Tasks(**task.dict(),owner_id=user.get('user_id'))
    db.add(newtask)
    db.commit()


@router.put('/updatetask/{taskid}',status_code=status.HTTP_204_NO_CONTENT)
async def update_task_of_user(user:user_dependency,db:db_dependency,tasktobeupdated:TaskRequest,taskid:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Unauthenticated!!')
    taskModel=db.query(Tasks).filter(taskid==Tasks.id).filter(Tasks.owner_id==user.get('user_id')).first()
    if taskModel is None:
        raise  HTTPException(status_code=404,detail='TASK WITH ID IS NOT FOUND!')
    taskModel.title=tasktobeupdated.title
    taskModel.description=tasktobeupdated.description
    taskModel.priority=tasktobeupdated.priority
    taskModel.complete=tasktobeupdated.complete
    db.add(taskModel)
    db.commit()
    
@router.delete('/deletetask/{taskid}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(user:user_dependency,db:db_dependency,taskid:int =Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Unauthenticated!!')   
    task=db.query(Tasks).filter(Tasks.id==taskid).filter(Tasks.owner_id==user.get('user_id')).first()
    if task is None:
        raise HTTPException(status_code=404,detail='Task with this id is not found!')
    db.query(Tasks).filter(Tasks.id==taskid).delete()
    db.commit()