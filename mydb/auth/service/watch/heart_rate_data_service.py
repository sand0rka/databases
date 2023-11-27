from http import HTTPStatus
from flask import abort
from mydb.auth.dao import heart_rate_data_dao
from mydb.auth.service.general_service import GeneralService


class HeartRateDataService(GeneralService):
    _dao = heart_rate_data_dao

    def get_heart_rate_data_by_user_id(self, user_id: int):
        heart_rate_data = self._dao.find_by_user_id(user_id)
        if heart_rate_data is None:
            abort(HTTPStatus.NOT_FOUND)
        return heart_rate_data
