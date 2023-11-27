from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class HeartRateData(IDto, db.Model):
    __tablename__ = "heart_rate_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    heart_rate_value = Column(Integer, nullable=True)
    timestamp = Column(DateTime, nullable=False)
    watch_owner_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates="heart_rate_data")

    def __repr__(self):
        return f"HeartRateData(id={self.id}, heart_rate_value={self.heart_rate_value}, " \
               f"timestamp={self.timestamp}, watch_owner_id={self.watch_owner_id}, user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> HeartRateData:
        obj = HeartRateData(
            id=dto_dict.get("id"),
            heart_rate_value=dto_dict.get("heart_rate_value"),
            timestamp=dto_dict.get("timestamp"),
            watch_owner_id=dto_dict.get("watch_owner_id"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "heart_rate_value": self.heart_rate_value,
            "timestamp": self.timestamp,
            "watch_owner_id": self.watch_owner_id,
            "user_id": self.user_id,
        }
