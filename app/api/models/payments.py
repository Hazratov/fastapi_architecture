from app.core.models.base import Base
from sqlalchemy import ForeignKey, Text, String,Integer, TIMESTAMP, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from typing import Optional
from datetime import datetime

class Payments(Base):
    __tablename__ = 'payments'
    booking_id = Mapped[int] = mapped_column(ForeignKey("bookings.id",ondelete="SET NULL"))
    payment_date = Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    amount = Mapped[float]
    payment_method = Mapped[str]
    status = Mapped[str]