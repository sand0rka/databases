from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import owner_controller
from mydb.auth.domain.watch.owner import Owner

owner_bp = Blueprint("owners", __name__, url_prefix="/owners/")


@owner_bp.get("")
def get_all_owners() -> Response:
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)


@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)


@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.patch('/<int:owner_id>')
def patch_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)


@owner_bp.post("")
def create_owner() -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_id = owner_controller.create(owner)
    return make_response(f"Owner created with ID: {owner_id}", HTTPStatus.CREATED)


@owner_bp.post("/bulk")
def create_all_owners() -> Response:
    content = request.get_json()
    owners = [Owner.create_from_dto(data) for data in content]
    owner_controller.create_all(owners)
    return make_response("All Owners created", HTTPStatus.CREATED)


@owner_bp.delete("/all")
def delete_all_owners() -> Response:
    owner_controller.delete_all()
    return make_response("All Owners deleted", HTTPStatus.OK)
