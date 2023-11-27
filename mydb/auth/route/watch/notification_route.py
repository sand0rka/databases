from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import notification_controller
from mydb.auth.domain.watch.notification import Notification

notification_bp = Blueprint("notifications", __name__, url_prefix="/notifications/")


@notification_bp.get("")
def get_all_notifications() -> Response:
    return make_response(jsonify(notification_controller.find_all()), HTTPStatus.OK)


@notification_bp.get('/<int:notification_id>')
def get_notification(notification_id: int) -> Response:
    return make_response(jsonify(notification_controller.find_by_id(notification_id)), HTTPStatus.OK)


@notification_bp.put('/<int:notification_id>')
def update_notification(notification_id: int) -> Response:
    content = request.get_json()
    notification = Notification.create_from_dto(content)
    notification_controller.update(notification_id, notification)
    return make_response("Notification updated", HTTPStatus.OK)


@notification_bp.patch('/<int:notification_id>')
def patch_notification(notification_id: int) -> Response:
    content = request.get_json()
    notification_controller.patch(notification_id, content)
    return make_response("Notification updated", HTTPStatus.OK)


@notification_bp.delete('/<int:notification_id>')
def delete_notification(notification_id: int) -> Response:
    notification_controller.delete(notification_id)
    return make_response("Notification deleted", HTTPStatus.OK)


@notification_bp.post("")
def create_notification() -> Response:
    content = request.get_json()
    notification = Notification.create_from_dto(content)
    notification_id = notification_controller.create(notification)
    return make_response(f"Notification created with ID: {notification_id}", HTTPStatus.CREATED)


@notification_bp.post("/bulk")
def create_all_notifications() -> Response:
    content = request.get_json()
    notifications = [Notification.create_from_dto(data) for data in content]
    notification_controller.create_all(notifications)
    return make_response(notification_controller.create_all(notifications), HTTPStatus.CREATED)


@notification_bp.delete("/all")
def delete_all_notifications() -> Response:
    notification_controller.delete_all()
    return make_response("All Notifications deleted", HTTPStatus.OK)
