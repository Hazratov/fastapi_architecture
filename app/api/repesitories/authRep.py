from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_general_session
from app.api.schemas.authSchema import authSchema
from sqlalchemy import text

class AuthRepository:
    def __init__(self, session : AsyncSession = Depends(get_general_session)) -> None:
        self.session = session

    async def create_user(self, data: dict) -> None:
        stat = text("insert into users(username,password,first_name,last_name,email,is_staff,is_active,is_superuser) values (:username,:password,:first_name,:last_name,:email,:is_staff,:is_active,:is_superuser)").bindparams(**data)
        await self.session.execute(stat)
        await self.session.commit()

    async def check_exist_user(self, username: str) -> bool:
        pass
