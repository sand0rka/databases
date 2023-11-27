from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.location_history import LocationHistory


class LocationHistoryDao(GeneralDAO):
    _domain_type = LocationHistory