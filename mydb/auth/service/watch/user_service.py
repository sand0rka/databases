from http import HTTPStatus
from flask import abort
from mydb.auth.dao import user_dao
from mydb.auth.service.general_service import GeneralService


class UserService(GeneralService):
    _dao = user_dao

    def get_user_by_relationship(self, relationship: str):
        user = self._dao.find_by_relationship(relationship)
        if user is None:
            abort(HTTPStatus.NOT_FOUND)
        return user
