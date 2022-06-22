from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.exercises import Exercise, ExerciseRepository
from src.domain.user import User, UserRepository


def test_return_two_types_of_exercises():
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    basic_exercise = Exercise(
        id="1",
        name="sentadillas",
        description="10 repeticiones",
        img="",
    )
    advanced_exercise = Exercise(
        id="21",
        name="curl de biceps",
        description="20 repeticiones",
        img="",
    )

    exercises_repository.save(basic_exercise)
    exercises_repository.save(advanced_exercise)

    response = client.get("/api/exercises")

    exercise_list = response.json
    assert len(exercise_list) == 2
    assert exercise_list[0]["id"] == "1"
    assert exercise_list[0]["name"] == "sentadillas"
    assert exercise_list[0]["description"] == "10 repeticiones"
    assert exercise_list[0]["img"] == ""

    assert exercise_list[1]["id"] == "21"
    assert exercise_list[1]["name"] == "curl de biceps"
    assert exercise_list[1]["description"] == "20 repeticiones"
    assert exercise_list[1]["img"] == ""

    return client
