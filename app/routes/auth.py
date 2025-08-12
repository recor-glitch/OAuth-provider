from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.schema.auth.user import UserCreate, UserPublic
from app.services.auth import Auth_Service
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/", response_model=UserPublic)
async def create_user(user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    auth = Auth_Service(db=db)
    try:
        user_result = await auth.create_user(user=user)
        return user_result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong, please try again.")