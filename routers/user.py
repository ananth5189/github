from fastapi import APIRouter,Depends,HTTPException,status,Path
import models
from models import Users,Tasks
from sqlalchemy.orm import session
from database import Base,engine,SessionLocal
from typing import Annotated
from pydantics.taskrequest import TaskRequest
from pydantics.userupdates import UserVerification,AddressUpdate
from .auth import get_current_user
from passlib.context import CryptContext


router=APIRouter(tags=['User Service'])

def get_db():
    db=SessionLocal()#open connection
    try:
        yield db
    finally:
        db.close()
bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')#setup info



db_dependency=Annotated[session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]

@router.get('/user/',status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=404,detail='user not Found!!')
    userinfo=db.query(Users).filter(Users.id==user.get('user_id')).first()
    if userinfo is None:
        raise HTTPException(status_code=404,detail='user not Found!!')
    userinfodict= db.query(Users).filter(Users.id==user.get('user_id')).first()
    return userinfodict

@router.put('/changepassword/',status_code=status.HTTP_200_OK)
async def change_password(user:user_dependency,db:db_dependency,userverification:UserVerification):
        if user is None:
            raise HTTPException(status_code=404,detail='user not Found!!')
        userinfo=db.query(Users).filter(Users.id==user.get('user_id')).first()
        if userinfo is None:
            raise HTTPException(status_code=404,detail='user not Found!!')
        if not bcrypt_context.verify(userverification.password,userinfo.hashed_password):
             raise HTTPException(status_code=201,detail='password change failed!!')
        userinfo.hashed_password=bcrypt_context.hash(userverification.new_password)
        db.add(userinfo)
        db.commit()
        
@router.put('/updateaddress/',status_code=status.HTTP_200_OK)
async def update_address(user:user_dependency,db:db_dependency,newaddress:AddressUpdate):
        if user is None:
            raise HTTPException(status_code=404,detail='user not Found!!')
        userinfo=db.query(Users).filter(Users.id==user.get('user_id')).first()
        userinfo.address=newaddress.address
        db.add(userinfo)
        db.commit()