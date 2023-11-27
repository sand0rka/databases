from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import watch_service


class WatchController(GeneralController):
    _service = watch_service
