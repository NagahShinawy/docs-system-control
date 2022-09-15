from flask_restful import Resource, reqparse
from models.user import CustomerModel
from utils import status
from utils.errors import (
    BLANK_ERROR,
    OBJ_MOT_FOUND,
    NAME_ALREADY_EXISTS,
)
from utils.success import CREATED_SUCCESSFULLY, UPDATED_SUCCESSFULLY

_customer_parser = reqparse.RequestParser()
_customer_parser.add_argument(
    "username", type=str, required=True, help=BLANK_ERROR.format("username")
)
_customer_parser.add_argument(
    "password", type=str, required=True, help=BLANK_ERROR.format("password")
)


class CustomerRegister(Resource):
    """
    create new user
    """

    def post(self):
        data = _customer_parser.parse_args()

        if CustomerModel.find_by_username(data["username"]):
            return {
                "message": NAME_ALREADY_EXISTS.format(
                    cls=self.__class__.__name__, name=data["username"]
                )
            }, status.HTTP_400_BAD_REQUEST

        customer = CustomerModel(**data)
        customer.save_to_db()

        return {"message": CREATED_SUCCESSFULLY}, status.HTTP_201_CREATED


class GetCustomer(Resource):
    @classmethod
    def get(cls, user_id: int):
        customer = CustomerModel.find_by_id(user_id)
        if not customer:
            return {
                "message": OBJ_MOT_FOUND.format(cls=cls.__name__)
            }, status.HTTP_404_NOT_FOUND
        return customer.json(), status.HTTP_200_OK


class DeleteCustomer(Resource):
    @classmethod
    def delete(cls, user_id: int):
        customer = CustomerModel.find_by_id(user_id)
        if not customer:
            return {
                "message": OBJ_MOT_FOUND.format(cls=cls.__name__)
            }, status.HTTP_404_NOT_FOUND
        customer.delete_from_db()
        return "", status.HTTP_204_NO_CONTENT


class PutCustomer(Resource):
    @classmethod
    def put(cls, user_id: int):
        customer = CustomerModel.find_by_id(user_id)
        if not customer:
            return {
                "message": OBJ_MOT_FOUND.format(cls=cls.__name__)
            }, status.HTTP_404_NOT_FOUND

        data = _customer_parser.parse_args()
        username = data.get("username")
        if username:
            customer.username = username

        password = data.get("password")
        if password:
            customer.password = password
        customer.save_to_db()
        return {
            "message": UPDATED_SUCCESSFULLY,
            "customer": customer.to_json(),
        }, status.HTTP_204_UPDATED
