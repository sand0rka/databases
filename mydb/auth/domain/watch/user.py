from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto

watch_users = db.Table(
    'watch_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('watch_id', db.Integer, db.ForeignKey('watch.id')),
    db.Column('watch_owner_id', db.Integer),
    extend_existing=True
)



class User(IDto, db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    phone_number = Column(String(13), unique=True, nullable=False)
    relationship_to_owner = Column(String(45), nullable=False)

    heart_rate_data = relationship("HeartRateData", back_populates="user")
    sleep_data = relationship("SleepData", back_populates="user")
    watches = db.relationship('Watch', secondary=watch_users, backref=db.backref('users_associated', lazy='dynamic'))

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"phone_number={self.phone_number}, relationship_to_owner={self.relationship_to_owner})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        obj = User(
            id=dto_dict.get("id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone_number=dto_dict.get("phone_number"),
            relationship_to_owner=dto_dict.get("relationship_to_owner"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "relationship_to_owner": self.relationship_to_owner,
        }
