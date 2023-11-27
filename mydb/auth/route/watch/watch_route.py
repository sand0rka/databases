from flask import Blueprint, Response, request, make_response, jsonify
from http import HTTPStatus

from mydb.auth.controller import watch_controller
from mydb.auth.domain.watch.watch import Watch

watch_bp = Blueprint("watches", __name__, url_prefix="/watches/")


@watch_bp.get("")
def get_all_watches() -> Response:
    return make_response(jsonify(watch_controller.find_all()), HTTPStatus.OK)


@watch_bp.get('/<int:watch_id>')
def get_watch(watch_id: int) -> Response:
    return make_response(jsonify(watch_controller.find_by_id(watch_id)), HTTPStatus.OK)


@watch_bp.put('/<int:watch_id>')
def update_watch(watch_id: int) -> Response:
    content = request.get_json()
    watch = Watch.create_from_dto(content)
    watch_controller.update(watch_id, watch)
    return make_response("Watch updated", HTTPStatus.OK)


@watch_bp.patch('/<int:watch_id>')
def patch_watch(watch_id: int) -> Response:
    content = request.get_json()
    watch_controller.patch(watch_id, content)
    return make_response("Watch updated", HTTPStatus.OK)


@watch_bp.delete('/<int:watch_id>')
def delete_watch(watch_id: int) -> Response:
    watch_controller.delete(watch_id)
    return make_response("Watch deleted", HTTPStatus.OK)


@watch_bp.post("")
def create_watch() -> Response:
    content = request.get_json()
    watch = Watch.create_from_dto(content)
    watch_id = watch_controller.create(watch)
    return make_response(f"Watch created with ID: {watch_id}", HTTPStatus.CREATED)


@watch_bp.post("/bulk")
def create_all_watches() -> Response:
    content = request.get_json()
    watches = [Watch.create_from_dto(data) for data in content]
    watch_controller.create_all(watches)
    return make_response("Watches created", HTTPStatus.CREATED)


@watch_bp.delete("/all")
def delete_all_watches() -> Response:
    watch_controller.delete_all()
    return make_response("All Watches deleted", HTTPStatus.OK)
