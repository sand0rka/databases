from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.watch import Watch


class WatchDao(GeneralDAO):
    _domain_type = Watch
