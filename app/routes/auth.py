from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.schema.auth.user import UserCreate
from app.services.auth import Auth_Service
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/")
async def create_user(user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    auth = Auth_Service(db=db)
    user = auth.create_user(user=user)

    if (user):
        return JSONResponse({"success": True, "data": user.model_dump_json()})
    return JSONResponse({"success": False, "data": "Something went wrong, please try again."})