from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.heart_rate_data import HeartRateData


class HeartRateDataDao(GeneralDAO):
    _domain_type = HeartRateData
