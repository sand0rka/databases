from http import HTTPStatus
from flask import abort
from mydb.auth.dao import sleep_data_dao
from mydb.auth.service.general_service import GeneralService


class SleepDataService(GeneralService):
    _dao = sleep_data_dao

    def get_sleep_data_by_user_id(self, user_id: int):
        sleep_data = self._dao.find_by_user_id(user_id)
        if sleep_data is None:
            abort(HTTPStatus.NOT_FOUND)
        return sleep_data
