from datetime import datetime, timedelta, timezone
from fastapi import APIRouter,Depends,HTTPException,status,Path
from pydantics.user import CreateUserRequest
from sqlalchemy.orm import session
from models import Users
import os
from passlib.context import CryptContext
from database import Base,engine,SessionLocal
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
from pydantics.tokens import Token
import secrets
from dotenv import load_dotenv


router=APIRouter(tags=['Authentication Service'])



bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer=OAuth2PasswordBearer(tokenUrl='auth/token')
load_dotenv('secrets.env')

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[session,Depends(get_db)]

def authenticate_user(db:db_dependency,username,password):
    user=db.query(Users).filter(Users.username==username).first()
    if user is None:
        return None
    if  bcrypt_context.verify(password,user.hashed_password):
        return user
    return None

def create_access_token(user_name:str,user_id:int,user_role:str,expires_delta:timedelta):
    encode={
        'sub':user_name,
        'id':user_id,
        'role':user_role
    }
    expires=datetime.now(timezone.utc)+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))

def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload=jwt.decode(token,os.getenv('SECRET_KEY'),algorithms=os.getenv('ALGORITHM'))
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        user_role:str=payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Unauthorised user')
        return {'username': username, 'user_id':user_id,'user_role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Unauthorised user')

user_dependency=Annotated[dict,Depends(get_current_user)]


@router.post('/signup',status_code=status.HTTP_201_CREATED)
async def createuser(user:user_dependency,newuserrequest:CreateUserRequest,db:db_dependency):
    if user is not None:
        raise HTTPException(status_code=403,detail='user already logged in')
    newusermodel=Users(
        username=newuserrequest.username,
        email=newuserrequest.email,
        firstname=newuserrequest.firstname,
        lastname=newuserrequest.lastname,
        hashed_password=bcrypt_context.hash(newuserrequest.password),
        role=newuserrequest.role,
        is_active=True
    )
    db.add(newusermodel)
    db.commit()


@router.post('/token',response_model=Token)
async def login_for_access_token(db:db_dependency,form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    authuser=  authenticate_user(db,form_data.username,form_data.password)
    if not authuser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Unauthorised user')
    jwttoken=create_access_token(authuser.username,authuser.id,authuser.role,timedelta(minutes=20))
    return {'access_token':jwttoken,'token_type':'bearer'}



