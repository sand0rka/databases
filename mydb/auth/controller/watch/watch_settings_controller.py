from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import watch_settings_service


class WatchSettingsController(GeneralController):
    _service = watch_settings_service
