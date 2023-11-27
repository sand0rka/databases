from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import location_history_service


class LocatonHistoryController(GeneralController):
    _service = location_history_service
