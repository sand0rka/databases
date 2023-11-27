from http import HTTPStatus
from flask import abort
from mydb.auth.dao import owner_dao
from mydb.auth.service.general_service import GeneralService


class OwnerService(GeneralService):
    _dao = owner_dao

    def get_user_by_phone_number(self, phone_number: str):
        owner = self._dao.find_by_phone_number(phone_number)
        if owner is None:
            abort(HTTPStatus.NOT_FOUND)
        return owner
