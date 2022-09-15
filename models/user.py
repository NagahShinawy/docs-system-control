from db import db
from typing import Dict, Union

customer_json = Dict[str, Union[int, str]]


class CrudModelMixin:
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class CustomerModel(CrudModelMixin, db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def json(self) -> customer_json:
        return {"id": self.id, "username": self.username}

    @classmethod
    def find_by_username(cls, username: str) -> "CustomerModel":  # return UserModel obj
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "CustomerModel":  # return list of UserModel objs
        return cls.query.filter_by(id=_id).first()
