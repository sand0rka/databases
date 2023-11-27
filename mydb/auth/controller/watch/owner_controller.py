from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import owner_service


class OwnerController(GeneralController):
    _service = owner_service
