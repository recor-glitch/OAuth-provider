from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schema.auth.user import UserBase, UserCreate
from app.utils.password import get_password_hash


class Auth_Service:
    def __init__(self, db: AsyncSession):
        self.db = db

    def create_organization():
        pass

    async def create_user(self, user: UserCreate) -> UserBase:
        try:
            password_hash = get_password_hash(user.password)

            self.db.add(User(**user.model_dump(exclude_unset=True), password_hash=password_hash))
            self.db.commit()
            return user.model_dump(exclude_unset=True)
        except:
            raise HTTPException(status_code=500, detail="unable to create the user, please try again")
