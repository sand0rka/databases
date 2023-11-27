from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto
from mydb.auth.domain.watch.notification import watch_notification
from mydb.auth.domain.watch.user import watch_users


class Watch(IDto, db.Model):
    __tablename__ = "watch"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String(255), nullable=False)
    serial_number = Column(String(45), unique=True, nullable=False)
    battery_level = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)

    owner = relationship("Owner", back_populates="watches")
    location_history = relationship(
        "LocationHistory",
        back_populates="watch",
        primaryjoin="and_(Watch.id == LocationHistory.watch_id, Watch.owner_id == LocationHistory.watch_owner_id)",
        lazy=True
    )
    watch_settings = relationship("WatchSettings", back_populates="watch",
                                  primaryjoin="Watch.id == WatchSettings.watch_id",
                                  foreign_keys="[WatchSettings.watch_id]",
                                  lazy=True)
    users = db.relationship('User', secondary=watch_users, backref=db.backref('watches_associated', lazy='dynamic'))
    notifications = relationship("Notification", secondary=watch_notification, backref="watches_associated")

    def __repr__(self):
        return f"Watch(id={self.id}, model={self.model}, serial_number={self.serial_number}, " \
               f"battery_level={self.battery_level}, owner_id={self.owner_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Watch:
        obj = Watch(
            id=dto_dict.get("id"),
            model=dto_dict.get("model"),
            serial_number=dto_dict.get("serial_number"),
            battery_level=dto_dict.get("battery_level"),
            owner_id=dto_dict.get("owner_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "serial_number": self.serial_number,
            "battery_level": self.battery_level,
            "owner_id": self.owner_id,
        }
