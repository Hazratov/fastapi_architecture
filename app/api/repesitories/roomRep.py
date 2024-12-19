from fastapi import Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.postgres.database import get_general_session

from app.api.schemas.roomschema import RoomsSchema


class RoomsRepository:
    def __init__(
            self,
            session: AsyncSession = Depends(get_general_session),
    ):
        self.session = session

    async def get_all_rooms(self):
        raw_sql = text("""
        SELECT m.room_number, s.title as room_type, m.price, f.title as status
        FROM rooms as m
        JOIN rooms_status as f ON m.status = f.id
        JOIN rooms_type as s ON m.room_type = s.id
        """)
        stmt = await self.session.execute(raw_sql)
        return [RoomsSchema.model_validate(map_res) for map_res in stmt.mappings().all()]

    async def get_room_by_id(self, room_id: int):
        raw_sql = text("""
        SELECT m.room_number, s.title as room_type, m.price, f.title as status
        FROM rooms as m
        JOIN rooms_status as f ON m.status = f.id
        JOIN rooms_type as s ON m.room_type = s.id
        WHERE m.id = :room_id
        """)
        stmt = await self.session.execute(raw_sql, {"room_id": room_id})
        result = stmt.mappings().first()  
        if not result:
            raise ValueError(f"{room_id} not found")
        return RoomsSchema.model_validate(result)
    