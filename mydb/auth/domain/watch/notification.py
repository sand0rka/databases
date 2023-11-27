from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto

watch_notification = db.Table(
    'watch_has_notification',
    db.Column('watch_id', db.Integer, db.ForeignKey('watch.id')),
    db.Column('watch_owner_id', db.Integer),
    db.Column('notification_id', db.Integer, db.ForeignKey('notification.id')),
    db.PrimaryKeyConstraint('watch_id', 'watch_owner_id', 'notification_id'),
    extend_existing=True
)


class Notification(IDto, db.Model):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    notification_type = Column(String(45), nullable=False)
    notification_message = Column(String(100), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    watches = relationship("Watch", secondary=watch_notification, backref="notifications_associated")

    def __repr__(self):
        return f"Notification(id={self.id}, notification_type={self.notification_type}, " \
               f"notification_message={self.notification_message}, timestamp={self.timestamp})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Notification:
        obj = Notification(
            id=dto_dict.get("id"),
            notification_type=dto_dict.get("notification_type"),
            notification_message=dto_dict.get("notification_message"),
            timestamp=dto_dict.get("timestamp"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "notification_type": self.notification_type,
            "notification_message": self.notification_message,
            "timestamp": self.timestamp,
        }
