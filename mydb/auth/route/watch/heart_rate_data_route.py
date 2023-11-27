from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import heart_rate_data_controller
from mydb.auth.domain.watch.heart_rate_data import HeartRateData

heart_rate_data_bp = Blueprint("heart_rate_data", __name__, url_prefix="/heart_rate_data/")


@heart_rate_data_bp.get("")
def get_all_heart_rate_data() -> Response:
    return make_response(jsonify(heart_rate_data_controller.find_all()), HTTPStatus.OK)


@heart_rate_data_bp.get('/<int:heart_rate_data_id>')
def get_heart_rate_data(heart_rate_data_id: int) -> Response:
    return make_response(jsonify(heart_rate_data_controller.find_by_id(heart_rate_data_id)), HTTPStatus.OK)


@heart_rate_data_bp.put('/<int:heart_rate_data_id>')
def update_heart_rate_data(heart_rate_data_id: int) -> Response:
    content = request.get_json()
    heart_rate_data = HeartRateData.create_from_dto(content)
    heart_rate_data_controller.update(heart_rate_data_id, heart_rate_data)
    return make_response("Heart rate data updated", HTTPStatus.OK)


@heart_rate_data_bp.patch('/<int:heart_rate_data_id>')
def patch_heart_rate_data(heart_rate_data_id: int) -> Response:
    content = request.get_json()
    heart_rate_data_controller.patch(heart_rate_data_id, content)
    return make_response("Heart rate data updated", HTTPStatus.OK)


@heart_rate_data_bp.delete('/<int:heart_rate_data_id>')
def delete_heart_rate_data(heart_rate_data_id: int) -> Response:
    heart_rate_data_controller.delete(heart_rate_data_id)
    return make_response("Heart rate data deleted", HTTPStatus.OK)


@heart_rate_data_bp.post("")
def create_heart_rate_data() -> Response:
    content = request.get_json()
    heart_rate_data = HeartRateData.create_from_dto(content)
    heart_rate_data_id = heart_rate_data_controller.create(heart_rate_data)
    return make_response(f"Heart rate data created with ID: {heart_rate_data_id}", HTTPStatus.CREATED)
