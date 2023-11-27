from http import HTTPStatus
from flask import abort
from mydb.auth.dao import watch_dao
from mydb.auth.service.general_service import GeneralService


class WatchService(GeneralService):
    _dao = watch_dao

    def get_watch_by_model(self, model: str):
        watch = self._dao.find_by_model(model)
        if watch is None:
            abort(HTTPStatus.NOT_FOUND)
        return watch

    def get_watch_by_serial_number(self, serial_number: str):
        watch = self._dao.find_by_serial_number(serial_number)
        if watch is None:
            abort(HTTPStatus.NOT_FOUND)
        return watch
