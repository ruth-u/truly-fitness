# from src.lib.utils import temp_file

# from src.webserver import create_app
# from src.domain.exercises import Exercise, ExerciseRepository


# def test_should_return_legs_exercise():
#     exercises_repository = ExerciseRepository(temp_file())
#     app = create_app(repositories={"exercises": exercises_repository})
#     client = app.test_client()

#     exercise1 = Exercise(
#         id=1,
#         name="sentadillas",
#         description="10 repeticiones",
#         img="",
#         category="pierna",
#     )
#     exercises_repository.save(exercise1)

#     exercise2 = Exercise(
#         id=8,
#         name="zancadas",
#         description="10 repeticiones",
#         img="",
#         category="pierna",
#     )

#     exercise3 = Exercise(
#         id=9, name="curl", description="10 repeticiones", img="", category="brazos"
#     )

#     exercises_repository.save(exercise2)
#     exercises_repository.save(exercise3)

#     response = client.get("/api/exercises_category")

#     print("*****", response.json)

#     exercise_list = response.json
#     assert len(exercise_list) == 2
#     assert exercise_list[0]["id"] == 1
#     assert exercise_list[0]["name"] == "sentadillas"
#     assert exercise_list[0]["description"] == "10 repeticiones"
#     assert exercise_list[0]["img"] == ""
#     assert exercise_list[0]["category"] == "pierna"

#     assert exercise_list[1]["id"] == 8
#     assert exercise_list[1]["name"] == "zancadas"
#     assert exercise_list[1]["description"] == "10 repeticiones"
#     assert exercise_list[1]["img"] == ""
#     assert exercise_list[0]["category"] == "pierna"
