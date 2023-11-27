from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class SleepData(IDto, db.Model):
    __tablename__ = "sleep_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sleep_start = Column(DateTime, nullable=False)
    sleep_finish = Column(DateTime, nullable=False)
    sleep_duration = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates="sleep_data")

    def __repr__(self):
        return f"SleepData(id={self.id}, sleep_start={self.sleep_start}, sleep_finish={self.sleep_finish}, " \
               f"sleep_duration={self.sleep_duration}, user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> SleepData:
        obj = SleepData(
            id=dto_dict.get("id"),
            sleep_start=dto_dict.get("sleep_start"),
            sleep_finish=dto_dict.get("sleep_finish"),
            sleep_duration=dto_dict.get("sleep_duration"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "sleep_start": self.sleep_start,
            "sleep_finish": self.sleep_finish,
            "sleep_duration": self.sleep_duration,
            "user_id": self.user_id,
        }
