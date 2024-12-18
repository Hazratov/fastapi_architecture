from app.core.models.base import Base
from sqlalchemy import ForeignKey, Text, String, Integer, TIMESTAMP, DECIMAL, BIGINT, Enum
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from typing import Optional
from datetime import datetime
from enum import Enum as PyEnum


class StatusEnum(PyEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class Bookings(Base):
    __tablename__ = "bookings"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'))
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id', ondelete="CASCADE"))
    check_in: Mapped[datetime]
    check_out: Mapped[datetime]
    total_price: Mapped[float]
    status: Mapped[StatusEnum] = mapped_column(Enum(StatusEnum))
