from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.models.user import User
from app.schema.auth.user import UserCreate, UserPublic, UserUpdate
from app.schema.base import BaseResponse
from app.utils.password import get_password_hash


class Auth_Service:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_organization():
        pass

    async def create_user(self, user: UserCreate) -> UserPublic:
        try:
            password_hash = get_password_hash(user.password)

            user_model = User(
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                password_hash=password_hash
            )

            self.db.add(user_model)
            await self.db.commit()
            await self.db.refresh(user_model)
            
            user_dict = {
                "id": user_model.id,
                "email": user_model.email,
                "first_name": user_model.first_name,
                "last_name": user_model.last_name,
                "created_at": user_model.created_at,
                "updated_at": user_model.updated_at
            }
            return UserPublic.model_validate(user_dict)
        except Exception as e:
            print(f"My error: {e}")
            raise HTTPException(status_code=500, detail="unable to create the user, please try again")
 

    async def update_user(self,  id: int, data: UserUpdate) -> BaseResponse:
        try:
            await self.db.execute(
                update(User)
                .where(User.id == id)
                .values(**data.model_dump(exclude_unset=True))
            )
            await self.db.commit()

            return BaseResponse(success=True, data="successfully updated the user")
        except:
            raise HTTPException(status_code=500, detail="something went wrong, try again latter.")
