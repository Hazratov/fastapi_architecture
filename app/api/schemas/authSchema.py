from pydantic import BaseModel


class authSchema(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    is_staff : bool
    is_active: bool
    is_superuser: bool

