from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.sleep_data import SleepData


class SleepDataDao(GeneralDAO):
    _domain_type = SleepData