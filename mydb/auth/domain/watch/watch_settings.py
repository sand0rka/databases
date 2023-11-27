from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class WatchSettings(IDto, db.Model):
    __tablename__ = "watch_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    home_address = Column(String(255), nullable=True)
    emergency_contact = Column(Text, nullable=True)
    watch_id = Column(Integer, nullable=False)
    watch_owner_id = Column(Integer, nullable=False)

    watch = relationship("Watch", back_populates="watch_settings",
                         primaryjoin="Watch.id == WatchSettings.watch_id",
                         foreign_keys="[WatchSettings.watch_id]",
                         lazy=True)

    def __repr__(self):
        return f"WatchSettings(id={self.id}, home_address={self.home_address}, " \
               f"emergency_contact={self.emergency_contact}, watch_id={self.watch_id}, " \
               f"watch_owner_id={self.watch_owner_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> WatchSettings:
        obj = WatchSettings(
            id=dto_dict.get("id"),
            home_address=dto_dict.get("home_address"),
            emergency_contact=dto_dict.get("emergency_contact"),
            watch_id=dto_dict.get("watch_id"),
            watch_owner_id=dto_dict.get("watch_owner_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "home_address": self.home_address,
            "emergency_contact": self.emergency_contact,
            "watch_id": self.watch_id,
            "watch_owner_id": self.watch_owner_id,
        }
