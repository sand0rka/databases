from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb.auth.controller import user_controller
from mydb.auth.domain.watch.user import User

user_bp = Blueprint("users", __name__, url_prefix="/users/")


@user_bp.get("")
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)


@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)


@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)


@user_bp.post("")
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_id = user_controller.create(user)
    return make_response(f"User created with ID: {user_id}", HTTPStatus.CREATED)


@user_bp.post("/bulk")
def create_all_users() -> Response:
    content = request.get_json()
    users = [User.create_from_dto(data) for data in content]
    user_controller.create_all(users)
    return make_response("All Users created", HTTPStatus.CREATED)


@user_bp.delete("/all")
def delete_all_users() -> Response:
    user_controller.delete_all()
    return make_response("All Users deleted", HTTPStatus.OK)
