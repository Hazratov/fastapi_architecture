from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BIGINT, String, Enum, Column, text
from enum import Enum as PyEnum
from datetime import datetime

# class UserRole(PyEnum):
#     ADMIN = "admin"
#     MANAGER = "manager"
#     RECEPTIONIST = "receptionist"
#     GUEST = "guest"
#     HOUSEKEEPER = "housekeeper"
#     AUDITOR = "auditor"
#     IT_SUPPORT = "it_support"


class Users(Base):
    __tablename__ = 'users'

    password: Mapped[str]
    username: Mapped[str] = mapped_column(String(150), unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(String(254), unique=True)
    is_staff: Mapped[bool]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))