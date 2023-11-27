from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.notification import Notification


class NotificationDao(GeneralDAO):
    _domain_type = Notification