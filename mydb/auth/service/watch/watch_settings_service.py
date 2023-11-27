from http import HTTPStatus
from flask import abort
from mydb.auth.dao import watch_settings_dao
from mydb.auth.service.general_service import GeneralService


class WatchSettingsService(GeneralService):
    _dao = watch_settings_dao

    def get_watch_settings_by_watch_id(self, watch_id: int):
        watch_settings = self._dao.find_by_watch_id(watch_id)
        if watch_settings is None:
            abort(HTTPStatus.NOT_FOUND)
        return watch_settings
