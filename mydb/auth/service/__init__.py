from mydb.auth.service.watch.watch_service import WatchService
from mydb.auth.service.watch.heart_rate_data_service import HeartRateDataService
from mydb.auth.service.watch.location_history_service import LocationHistoryService
from mydb.auth.service.watch.notification_service import NotificationService
from mydb.auth.service.watch.owner_service import OwnerService
from mydb.auth.service.watch.sleep_data_service import SleepDataService
from mydb.auth.service.watch.user_service import UserService
from mydb.auth.service.watch.watch_settings_service import WatchSettingsService

watch_service = WatchService()
heart_rate_data_service = HeartRateDataService()
location_history_service = LocationHistoryService()
notification_service = NotificationService()
owner_service = OwnerService()
sleep_data_service = SleepDataService()
user_service = UserService()
watch_settings_service = WatchSettingsService()
