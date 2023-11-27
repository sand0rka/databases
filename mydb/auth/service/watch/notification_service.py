from http import HTTPStatus
from flask import abort
from mydb.auth.dao import notification_dao
from mydb.auth.service.general_service import GeneralService


class NotificationService(GeneralService):
    _dao = notification_dao

    def get_notification_by_type(self, notification_type: str):
        notification = self._dao.find_by_type(notification_type)
        if notification is None:
            abort(HTTPStatus.NOT_FOUND)
        return notification
