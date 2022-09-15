import os
from flask import Flask
from flask_restful import Api
from flask_mysqldb import MySQL


from db import db
from resources.user import UserRegister, User
from utils import status

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB")

mysql = MySQL(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "SOMETHING"
api = Api(app)


api.add_resource(UserRegister, "/register/")
api.add_resource(User, "/user/<int:user_id>/")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5060, debug=True, use_reloader=True)
