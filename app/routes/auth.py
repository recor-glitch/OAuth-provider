from typing import Annotated
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.schema.auth.user import UserCreate, UserPublic, UserUpdate
from app.schema.base import BaseResponse
from app.services.auth import Auth_Service
from app.core.db import get_db

router = APIRouter()
db_anotation = Annotated[AsyncSession, Depends(get_db)]

@router.post("/", response_model=UserPublic)
async def create_user(user: UserCreate, db: db_anotation):
    auth = Auth_Service(db=db)
    user_result = await auth.create_user(user=user)
    return user_result
    
@router.patch("/{id}", response_model=BaseResponse)
async def update_user(update_user: UserUpdate, id: int, db: db_anotation):
    auth = Auth_Service(db=db)
    return await auth.update_user(id=id, data=update_user)