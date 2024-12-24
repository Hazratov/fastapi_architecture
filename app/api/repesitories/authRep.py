from fastapi import Depends, HTTPException, status
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

    async def get_user_if_exists(self, username: str) -> bool:
        stmt = text("select * from users where username = :username").bindparams(username=username)
        res = await self.session.execute(
            stmt
        )
        mapped_result = res.mappings().first()

        if not mapped_result:
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail="Not Authorized"
            )
        return self.serializer.serialize(mapped_result)

    