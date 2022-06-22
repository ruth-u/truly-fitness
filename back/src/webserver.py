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

    @app.route("/api/exercises/<id>", methods=["GET"])
    def exercises_get_by_id(id):
        exercises = repositories["exercises"].get_exercise_by_id(id)
        return object_to_json(exercises)

    @app.route("/api/plan", methods=["GET"])
    def exercises_by_exeperiencie():
        user_no_experiencie = repositories["users"].get_user_by_experiencie(0)
        user_with_experiencie = repositories["users"].get_user_by_experiencie(1)
        basic_exercises = repositories["exercises"].get_basic_exercises()
        advanced_exercises = repositories["exercises"].get_advanced_exercises()

        if user_no_experiencie:
            return object_to_json(basic_exercises)
        elif user_with_experiencie:
            return object_to_json(advanced_exercises)
        else:
            return "", 401

    return app
