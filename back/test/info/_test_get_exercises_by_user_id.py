from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.exercises import Exercise, ExerciseRepository


def test_should_return_a_exercises_by_user_id():
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    exercise1 = Exercise(
        id="000",
        user_id="uu1",
        name="sentadillas",
        description="10 repeticiones",
        img="",
        week_day="1",
        week="1",
    )
    exercises_repository.save(exercise1)

    response = client.get("/api/exercises")

    exercise_list = response.json
    assert len(exercise_list) == 2
    assert exercise_list[0]["id"] == "000"
    assert exercise_list[0]["name"] == "sentadillas"
    assert exercise_list[0]["description"] == "10 repeticiones"
    assert exercise_list[0]["img"] == ""
    assert exercise_list[0]["week_day"] == "1"
    assert exercise_list[0]["week"] == "1"
