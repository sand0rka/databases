from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import notification_service


class NotificationController(GeneralController):
    _service = notification_service
