from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.owner import Owner


class OwnerDao(GeneralDAO):
    _domain_type = Owner