from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .watch.watch_route import watch_bp
    from .watch.heart_rate_data_route import heart_rate_data_bp
    from .watch.location_history_route import location_history_bp
    from .watch.notification_route import notification_bp
    from .watch.owner_route import owner_bp
    from .watch.sleep_data_route import sleep_data_bp
    from .watch.user_route import user_bp
    from .watch.watch_settings_route import watch_settings_bp

    app.register_blueprint(watch_bp)
    app.register_blueprint(heart_rate_data_bp)
    app.register_blueprint(location_history_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(sleep_data_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(watch_settings_bp)


