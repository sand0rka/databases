from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import sleep_data_service


class SleepDataController(GeneralController):
    _service = sleep_data_service
