from .watch.watch_dao import WatchDao
from .watch.watch_settings_dao import WatchSettingsDao
from .watch.user_dao import UserDao
from .watch.sleep_data_dao import SleepDataDao
from .watch.owner_dao import OwnerDao
from .watch.notification_dao import NotificationDao
from .watch.location_history_dao import LocationHistoryDao
from .watch.heart_rate_data_dao import HeartRateDataDao

watch_dao = WatchDao()
watch_settings_dao = WatchSettingsDao()
user_dao = UserDao()
sleep_data_dao = SleepDataDao()
owner_dao = OwnerDao()
notification_dao = NotificationDao()
location_history_dao = LocationHistoryDao()
heart_rate_data_dao = HeartRateDataDao()
