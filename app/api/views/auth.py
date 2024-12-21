from fastapi import APIRouter
from fastapi import status, Depends

from app.api.schemas.authSchema import authSchema
from app.api.controller.controllerAuth import AuthController

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(data: authSchema, controller: AuthController = Depends()):
    return await controller.create_user(data=data)


@router.post("/token", status_code=status.HTTP_200_OK)
async def get_token():
    pass