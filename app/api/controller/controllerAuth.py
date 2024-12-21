from app.api.repesitories.authRep import AuthRepository
from app.api.schemas.authSchema import authSchema
from fastapi import Depends
from passlib.hash import bcrypt


class AuthController:
    def __init__(self, auth_repo : AuthRepository = Depends()) -> None:
        self.auth_repo = auth_repo

    async def create_user(self, data : authSchema) -> None:
        data.password = bcrypt.hash(data.password)
        return await self.auth_repo.create_user(data=data.model_dump())
    