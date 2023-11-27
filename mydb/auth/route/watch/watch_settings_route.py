from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import watch_settings_controller
from mydb.auth.domain.watch.watch_settings import WatchSettings

watch_settings_bp = Blueprint("watch_settings", __name__, url_prefix="/watch-settings/")


@watch_settings_bp.get("")
def get_all_watch_settings() -> Response:
    return make_response(jsonify(watch_settings_controller.find_all()), HTTPStatus.OK)


@watch_settings_bp.get('/<int:watch_settings_id>')
def get_watch_settings(watch_settings_id: int) -> Response:
    return make_response(jsonify(watch_settings_controller.find_by_id(watch_settings_id)), HTTPStatus.OK)


@watch_settings_bp.put('/<int:watch_settings_id>')
def update_watch_settings(watch_settings_id: int) -> Response:
    content = request.get_json()
    watch_settings = WatchSettings.create_from_dto(content)
    watch_settings_controller.update(watch_settings_id, watch_settings)
    return make_response("Watch settings updated", HTTPStatus.OK)


@watch_settings_bp.patch('/<int:watch_settings_id>')
def patch_watch_settings(watch_settings_id: int) -> Response:
    content = request.get_json()
    watch_settings_controller.patch(watch_settings_id, content)
    return make_response("Watch settings updated", HTTPStatus.OK)


@watch_settings_bp.delete('/<int:watch_settings_id>')
def delete_watch_settings(watch_settings_id: int) -> Response:
    watch_settings_controller.delete(watch_settings_id)
    return make_response("Watch settings deleted", HTTPStatus.OK)


@watch_settings_bp.post("")
def create_watch_settings() -> Response:
    content = request.get_json()
    watch_settings = WatchSettings.create_from_dto(content)
    watch_settings_id = watch_settings_controller.create(watch_settings)
    return make_response(f"Watch settings created with ID: {watch_settings_id}", HTTPStatus.CREATED)
