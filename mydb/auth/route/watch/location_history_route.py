from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from mydb.auth.controller import location_history_controller

location_history_bp = Blueprint("location_history", __name__, url_prefix="/location-history/")


@location_history_bp.get("")
def get_all_location_history() -> Response:
    return make_response(jsonify(location_history_controller.find_all()), HTTPStatus.OK)


@location_history_bp.get('/<int:location_history_id>')
def get_location_history(location_history_id: int) -> Response:
    return make_response(jsonify(location_history_controller.find_by_id(location_history_id)), HTTPStatus.OK)


@location_history_bp.put('/<int:location_history_id>')
def update_location_history(location_history_id: int) -> Response:
    content = request.get_json()
    location_history_controller.update(location_history_id, content)
    return make_response("Location history updated", HTTPStatus.OK)


@location_history_bp.patch('/<int:location_history_id>')
def patch_location_history(location_history_id: int) -> Response:
    content = request.get_json()
    location_history_controller.patch(location_history_id, content)
    return make_response("Location history updated", HTTPStatus.OK)


@location_history_bp.delete('/<int:location_history_id>')
def delete_location_history(location_history_id: int) -> Response:
    location_history_controller.delete(location_history_id)
    return make_response("Location history deleted", HTTPStatus.OK)


@location_history_bp.post("")
def create_location_history() -> Response:
    content = request.get_json()
    location_history_controller.create(content)
    return make_response("Location history created", HTTPStatus.CREATED)


@location_history_bp.post("/bulk")
def create_all_location_history() -> Response:
    content = request.get_json()
    location_history_controller.create_all(content)
    return make_response("Location history created", HTTPStatus.CREATED)


@location_history_bp.get("/watch/<int:watch_id>/owner/<int:watch_owner_id>")
def get_location_history_for_watch(watch_id: int, watch_owner_id: int) -> Response:
    return make_response(jsonify(location_history_controller.find_by_watch(watch_id, watch_owner_id)), HTTPStatus.OK)
