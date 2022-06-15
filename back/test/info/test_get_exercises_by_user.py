from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.user import User, UserRepository
from src.domain.exercises import Exercise, ExerciseRepository
from src.domain.user_exercises import UserExercise, UserExerciseRepository


def setup_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})

    client = app.test_client()

    christian = User(
        id="uu1",
        first_name="Christian",
        last_name="Garcia",
        user_name="chris11",
        password="chris123",
        goal="ganar peso",
        weight="70",
        height="185",
        experiencie=1,
    )
    user_repository.save(christian)
    return client


def setup_exercises():
    exercises_repository = ExerciseRepository(temp_file())
    app = create_app(repositories={"exercises": exercises_repository})
    client = app.test_client()

    exercise1 = Exercise(
        id="8",
        user_id="uu1",
        name="sentadillas",
        description="20 repeticiones",
        img="",
    )

    exercise2 = Exercise(
        id="9",
        user_id="uu1",
        name="hip trhust",
        description="20 repeticiones",
        img="",
    )

    exercise3 = Exercise(
        id="10",
        user_id="uu1",
        name="peso muerto",
        description="25 repeticiones",
        img="",
    )

    exercise4 = Exercise(
        id="11",
        user_id="uu1",
        name="hip thrust",
        description="20 repeticiones",
        img="",
    )

    exercise5 = Exercise(
        id="12",
        user_id="uu1",
        name="patadas de burro",
        description="20 repeticiones",
        img="",
    )

    exercise6 = Exercise(
        id="13",
        user_id="uu1",
        name="dominadas",
        description="10 repeticiones",
        img="",
    )
    exercise7 = Exercise(
        id="14",
        user_id="uu1",
        name="curl",
        description="20 repeticiones",
        img="",
    )
    exercise8 = Exercise(
        id="15",
        user_id="uu1",
        name="abdominales",
        description="20 repeticiones",
        img="",
    )

    exercises_repository.save(exercise1)
    exercises_repository.save(exercise2)
    exercises_repository.save(exercise3)
    exercises_repository.save(exercise4)
    exercises_repository.save(exercise5)
    exercises_repository.save(exercise6)
    exercises_repository.save(exercise7)
    exercises_repository.save(exercise8)

    return client


def test_should_return_a_plan_by_date():
    exercises_repository = UserExerciseRepository(temp_file())
    app = create_app(repositories={"users_exercises": exercises_repository})
    client = app.test_client()

    first_day_plan = UserExercise(
        user_id="uu1",
        exercise_id="8",
        exercise_date="2022-06-09",
        done=False,
    )

    other_first_day_plan = UserExercise(
        user_id="uu1",
        exercise_id="9",
        exercise_date="2022-06-09",
        done=False,
    )

    second_day_plan = UserExercise(
        user_id="uu1",
        exercise_id="10",
        exercise_date="2022-06-010",
        done=False,
    )

    third_day_plan = UserExercise(
        user_id="uu1",
        exercise_id="11",
        exercise_date="2022-06-11",
        done=False,
    )
    # fourth_day_plan = Exercise(
    #     user_id="uu1",
    #     exercise_id="12",
    #     exercise_date="2022-06-12",
    #     exercise_done=False,
    # )
    # fifth_day_plan = Exercise(
    #     user_id="uu1",
    #     exercise_id="13",
    #     exercise_date="2022-06-13",
    #     exercise_done=False,
    # )
    # sixth_day_plan = Exercise(
    #     user_id="uu1",
    #     exercise_id="14",
    #     exercise_date="2022-06-14",
    #     exercise_done=False,
    # )
    # seventh_day_plan = Exercise(
    #     user_id="uu1",
    #     exercise_id="15",
    #     exercise_date="2022-06-15",
    #     exercise_done=False,
    # )

    exercises_repository.save_user_exercises(first_day_plan)
    exercises_repository.save_user_exercises(other_first_day_plan)
    exercises_repository.save_user_exercises(second_day_plan)
    exercises_repository.save_user_exercises(third_day_plan)
    # exercises_repository.save_exercise_by_date(fourth_day_plan)
    # exercises_repository.save_exercise_by_date(fifth_day_plan)
    # exercises_repository.save_exercise_by_date(sixth_day_plan)
    # exercises_repository.save_exercise_by_date(seventh_day_plan)

    response = client.get("/api/my_plan")

    exercise_list = response.json
    assert len(exercise_list) == 4
    assert exercise_list[0]["user_id"] == "uu1"
    assert exercise_list[0]["exercise_id"] == "8"

    assert exercise_list[0]["exercise_date"] == "2022-06-09"
    assert exercise_list[0]["done"] == False

    assert exercise_list[0]["user_id"] == "uu1"
    assert exercise_list[0]["exercise_id"] == "9"
    assert exercise_list[0]["exercise_date"] == "2022-06-09"
    assert exercise_list[0]["done"] == False

    assert exercise_list[0]["user_id"] == "uu1"
    assert exercise_list[0]["exercise_id"] == "10"
    assert exercise_list[0]["exercise_date"] == "2022-06-10"
    assert exercise_list[0]["done"] == False

    assert exercise_list[0]["user_id"] == "uu1"
    assert exercise_list[0]["exercise_id"] == "11"
    assert exercise_list[0]["exercise_date"] == "2022-06-11"
    assert exercise_list[0]["done"] == ""
