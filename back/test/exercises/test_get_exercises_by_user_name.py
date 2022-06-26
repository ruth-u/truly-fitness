from src.lib.utils import temp_file, object_to_json
from src.webserver import create_app
from src.domain.user import User, UserRepository
from src.domain.exercises import Exercise, ExerciseRepository


def test_should_get_exercises_for_experiencied_user():
    database = temp_file()
    users_repository = UserRepository(database)
    exercises_repository = ExerciseRepository(database)
    app = create_app(
        repositories={"users": users_repository, "exercises": exercises_repository}
    )
    client = app.test_client()

    christian = User(
        id=1,
        user_name="christian",
        password="chris123",
        first_name="christian",
        last_name="garcia",
        goal="ganar peso",
        weight="70",
        height="185",
        experiencie=1,
        register_date="2022-06-07",
    )

    users_repository.save(christian)

    advanced_exercise = Exercise(
        id=21,
        name="curl de biceps",
        description="20 repeticiones",
        img="",
        category="brazos",
    )
    basic_exercise = Exercise(
        id=1,
        name="sentadillas",
        description="10 repeticiones",
        img="",
        category="piernas",
    )
    exercises_repository.save(advanced_exercise)
    exercises_repository.save(basic_exercise)
    response = client.get("/api/plan/christian")

    exercise_list = response.json
    assert len(exercise_list) == 1
    assert exercise_list[0]["id"] == 21
    assert exercise_list[0]["name"] == "curl de biceps"
    assert exercise_list[0]["description"] == "20 repeticiones"
    assert exercise_list[0]["img"] == ""
    assert exercise_list[0]["category"] == "brazos"


def test_should_get_exercises_for_unexperiencied_user():
    users_repository = UserRepository(temp_file())
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(
        repositories={"users": users_repository, "exercises": exercises_repository}
    )
    client = app.test_client()

    nagore = User(
        id=2,
        user_name="nagore.c",
        password="nagore123",
        first_name="nagore",
        last_name="garcia",
        goal="ganar peso",
        weight="70",
        height="185",
        experiencie=0,
        register_date="2022-06-07",
    )

    users_repository.save(nagore)

    advanced_exercise = Exercise(
        id=21,
        name="curl de biceps",
        description="20 repeticiones",
        img="",
        category="brazos",
    )
    basic_exercise = Exercise(
        id=1,
        name="sentadillas",
        description="10 repeticiones",
        img="",
        category="piernas",
    )
    exercises_repository.save(advanced_exercise)
    exercises_repository.save(basic_exercise)
    response = client.get("/api/plan/nagore.c")

    exercise_list = response.json
    assert len(exercise_list) == 1
    assert exercise_list[0]["id"] == 1
    assert exercise_list[0]["name"] == "sentadillas"
    assert exercise_list[0]["description"] == "10 repeticiones"
    assert exercise_list[0]["img"] == ""
    assert exercise_list[0]["category"] == "piernas"
