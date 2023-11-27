from mydb.auth.controller.watch.watch_controller import WatchController
from mydb.auth.controller.watch.heart_rate_data_controller import HeartRateDataController
from mydb.auth.controller.watch.location_history_controller import LocatonHistoryController
from mydb.auth.controller.watch.notification_controller import NotificationController
from mydb.auth.controller.watch.owner_controller import OwnerController
from mydb.auth.controller.watch.sleep_data_controller import SleepDataController
from mydb.auth.controller.watch.user_controller import UserController
from mydb.auth.controller.watch.watch_settings_controller import WatchSettingsController

watch_controller = WatchController()
heart_rate_data_controller = HeartRateDataController()
location_history_controller = LocatonHistoryController()
notification_controller = NotificationController()
owner_controller = OwnerController()
sleep_data_controller = SleepDataController()
user_controller = UserController()
watch_settings_controller = WatchSettingsController()
