from flask import Flask, request
from flask_cors import CORS


from src.lib.utils import object_to_json
from src.domain.user import User, UserRepository
from src.domain.exercises import Exercise, ExerciseRepository


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_by_user_name(body["user_name"])
        if user is None or body["password"] != user.password:
            return "", 401
        else:
            return user.to_dict(), 200

    @app.route("/api/users", methods=["GET"])
    def users_get():
        users = repositories["users"].get_users()
        return object_to_json(users)

    @app.route("/api/users", methods=["POST"])
    def contacts_post():
        user_id = request.headers.get("Authorization")

        body = request.json
        user = User(
            id=user_id,
            user_name=body["user_name"],
            password=body["password"],
            first_name=body["first_name"],
            last_name=body["last_name"],
            goal=body["goal"],
            weight=body["weight"],
            height=body["height"],
            experiencie=body["experiencie"],
            register_date=body["register_date"],
        )

        if user.id == user_id:
            repositories["users"].save(user)
            return "", 200

        else:
            return "", 403

    @app.route("/api/exercises", methods=["GET"])
    def exercises_get():
        exercises = repositories["exercises"].get_exercises()

        return object_to_json(exercises)

    # @app.route("/api/users/<id>", methods=["GET"])
    # def users_get_by_id(id):
    #     user_id = request.headers.get("Autorization")
    #     user = repositories["users"].get_users_by_id(id)

    #     if user_id == user.user_id:
    #         return object_to_json(user), 200
    #     else:
    #         return "", 403

    return app
