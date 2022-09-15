from flask_restful import Resource, reqparse
from models.user import UserModel
from utils import status
from utils.errors import (
    BLANK_ERROR,
    OBJ_MOT_FOUND,
    NAME_ALREADY_EXISTS,
)
from utils.success import CREATED_SUCCESSFULLY

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", type=str, required=True, help=BLANK_ERROR.format("username")
)
_user_parser.add_argument(
    "password", type=str, required=True, help=BLANK_ERROR.format("password")
)


class UserRegister(Resource):
    """
    create new user
    """

    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {
                "message": NAME_ALREADY_EXISTS.format(
                    cls=self.__class__.__name__, name=data["username"]
                )
            }, status.HTTP_400_BAD_REQUEST

        user = UserModel(**data)
        user.save_to_db()

        return {"message": CREATED_SUCCESSFULLY}, status.HTTP_201_CREATED


class User(Resource):
    """
    Get, Delete user method
    """

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {
                "message": OBJ_MOT_FOUND.format(cls=cls.__name__)
            }, status.HTTP_404_NOT_FOUND
        return user.json(), status.HTTP_200_OK

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {
                "message": OBJ_MOT_FOUND.format(cls=cls.__name__)
            }, status.HTTP_404_NOT_FOUND
        user.delete_from_db()
        return "", status.HTTP_204_NO_CONTENT
