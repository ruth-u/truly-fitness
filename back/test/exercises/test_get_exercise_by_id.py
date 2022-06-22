from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.exercises import Exercise, ExerciseRepository


def test_should_return_a_exercises_by_id():
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    exercise1 = Exercise(
        id=1,
        name="sentadillas",
        description="10 repeticiones",
        img="",
        category="pierna",
    )
    exercises_repository.save(exercise1)

    exercise2 = Exercise(
        id=2,
        name="correr",
        description="20 minutos",
        img="",
        category="hit",
    )
    exercises_repository.save(exercise2)
    response = client.get("/api/exercises/1")
    print(response.json, "holiiiiiii")

    exercise_dic = response.json
    assert exercise_dic["id"] == 1
    assert exercise_dic["name"] == "sentadillas"
    assert exercise_dic["description"] == "10 repeticiones"
    assert exercise_dic["img"] == ""
    assert exercise_dic["category"] == "pierna"
