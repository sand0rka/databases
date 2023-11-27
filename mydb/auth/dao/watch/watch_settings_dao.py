from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.watch_settings import WatchSettings


class WatchSettingsDao(GeneralDAO):
    _domain_type = WatchSettings