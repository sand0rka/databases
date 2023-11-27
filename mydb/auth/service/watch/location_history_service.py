from http import HTTPStatus
from flask import abort
from mydb.auth.dao import location_history_dao
from mydb.auth.service.general_service import GeneralService


class LocationHistoryService(GeneralService):
    _dao = location_history_dao

    def get_location_history_by_watch_id(self, watch_id: int):
        location_history = self._dao.find_by_watch_id(watch_id)
        if location_history is None:
            abort(HTTPStatus.NOT_FOUND)
        return location_history
