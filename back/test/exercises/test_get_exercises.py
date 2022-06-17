from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.exercises import Exercise, ExerciseRepository


def test_should_return_empty_list_of_exercises():

    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    response = client.get("/api/exercises")

    assert response.json == []


def test_should_return_exercises():
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    exercise1 = Exercise(
        id="000",
        name="sentadillas",
        description="10 repeticiones",
        img="",
    )
    exercises_repository.save(exercise1)

    exercise2 = Exercise(
        id="008",
        name="zancadas",
        description="10 repeticiones",
        img="",
    )

    exercises_repository.save(exercise2)

    response = client.get("/api/exercises")

    exercise_list = response.json
    assert len(exercise_list) == 2
    assert exercise_list[0]["id"] == "000"
    assert exercise_list[0]["name"] == "sentadillas"
    assert exercise_list[0]["description"] == "10 repeticiones"
    assert exercise_list[0]["img"] == ""

    assert exercise_list[1]["id"] == "008"
    assert exercise_list[1]["name"] == "zancadas"
    assert exercise_list[1]["description"] == "10 repeticiones"
    assert exercise_list[1]["img"] == ""
