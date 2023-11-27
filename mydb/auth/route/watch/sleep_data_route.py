from flask import Blueprint, Response, request, make_response, jsonify
from http import HTTPStatus
from mydb.auth.controller import sleep_data_controller
from mydb.auth.domain.watch.sleep_data import SleepData

sleep_data_bp = Blueprint("sleep_data", __name__, url_prefix="/sleep-data/")


@sleep_data_bp.get("")
def get_all_sleep_data() -> Response:
    return make_response(jsonify(sleep_data_controller.find_all()), HTTPStatus.OK)


@sleep_data_bp.get('/<int:sleep_data_id>')
def get_sleep_data(sleep_data_id: int) -> Response:
    return make_response(jsonify(sleep_data_controller.find_by_id(sleep_data_id)), HTTPStatus.OK)


@sleep_data_bp.put('/<int:sleep_data_id>')
def update_sleep_data(sleep_data_id: int) -> Response:
    content = request.get_json()
    sleep_data = SleepData.create_from_dto(content)
    sleep_data_controller.update(sleep_data_id, sleep_data)
    return make_response("Sleep data updated", HTTPStatus.OK)


@sleep_data_bp.patch('/<int:sleep_data_id>')
def patch_sleep_data(sleep_data_id: int) -> Response:
    content = request.get_json()
    sleep_data_controller.patch(sleep_data_id, content)
    return make_response("Sleep data updated", HTTPStatus.OK)


@sleep_data_bp.delete('/<int:sleep_data_id>')
def delete_sleep_data(sleep_data_id: int) -> Response:
    sleep_data_controller.delete(sleep_data_id)
    return make_response("Sleep data deleted", HTTPStatus.OK)


@sleep_data_bp.post("")
def create_sleep_data() -> Response:
    content = request.get_json()
    sleep_data = SleepData.create_from_dto(content)
    sleep_data_id = sleep_data_controller.create(sleep_data)
    return make_response(f"Sleep data created with ID: {sleep_data_id}", HTTPStatus.CREATED)


@sleep_data_bp.post("/bulk")
def create_all_sleep_data() -> Response:
    content = request.get_json()
    sleep_data_list = [SleepData.create_from_dto(data) for data in content]
    sleep_data_controller.create_all(sleep_data_list)
    return make_response("Sleep data created", HTTPStatus.CREATED)


@sleep_data_bp.delete("/all")
def delete_all_sleep_data() -> Response:
    sleep_data_controller.delete_all()
    return make_response("All sleep data deleted", HTTPStatus.OK)
