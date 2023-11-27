from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import heart_rate_data_service


class HeartRateDataController(GeneralController):
    _service = heart_rate_data_service
