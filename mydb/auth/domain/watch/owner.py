from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Owner(IDto, db.Model):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    phone_number = Column(String(13), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    watches = relationship("Watch", back_populates="owner")

    def __repr__(self):
        return f"Owner(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"phone_number={self.phone_number}, email={self.email})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Owner:
        obj = Owner(
            id=dto_dict.get("id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone_number=dto_dict.get("phone_number"),
            email=dto_dict.get("email"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
        }
