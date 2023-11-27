from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class LocationHistory(IDto, db.Model):
    __tablename__ = "location_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(DECIMAL(11, 6), nullable=False)
    latitude = Column(DECIMAL(10, 6), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    watch_id = Column(Integer, ForeignKey('watch.id'), nullable=False)
    watch_owner_id = Column(Integer, ForeignKey('watch.owner_id'), nullable=False)

    watch = relationship("Watch", back_populates="location_history",
                         primaryjoin="and_(LocationHistory.watch_id == Watch.id, LocationHistory.watch_owner_id == Watch.owner_id)",
                         foreign_keys="[LocationHistory.watch_id, LocationHistory.watch_owner_id]")

    def __repr__(self):
        return f"LocationHistory(id={self.id}, longitude={self.longitude}, latitude={self.latitude}, " \
               f"timestamp={self.timestamp}, watch_id={self.watch_id}, watch_owner_id={self.watch_owner_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> LocationHistory:
        obj = LocationHistory(
            id=dto_dict.get("id"),
            longitude=dto_dict.get("longitude"),
            latitude=dto_dict.get("latitude"),
            timestamp=dto_dict.get("timestamp"),
            watch_id=dto_dict.get("watch_id"),
            watch_owner_id=dto_dict.get("watch_owner_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "timestamp": self.timestamp,
            "watch_id": self.watch_id,
            "watch_owner_id": self.watch_owner_id,
        }
