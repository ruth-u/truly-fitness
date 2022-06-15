import sys

sys.path.insert(0, "")


def main():

    from src.domain.user import User, UserRepository

    database_path = "data/database.db"
    users_repository = UserRepository(database_path)

    christian = User(
        id="uu1",
        first_name="Christian",
        last_name="Garcia",
        user_name="chris11",
        password="chris123",
        goal="loose_weight",
        weight="110",
        height="185",
        experiencie=1,
        register_date="2022-06-07",
    )
    nagore = User(
        id="uu2",
        first_name="Nagore",
        last_name="Cuevas",
        user_name="nagore.c",
        password="nagore123",
        goal="gain_weight",
        weight="48",
        height="165",
        experiencie=0,
        register_date="2022-06-07",
    )

    users_repository.save(christian)
    users_repository.save(nagore)

    from src.domain.exercises import Exercise, ExerciseRepository

    database_path = "data/database.db"
    exercises_repository = ExerciseRepository(database_path)

    exercise5 = Exercise(
        id="5",
        name="Sentadillas",
        description="20 repeticiones",
        img="",
    )
    exercise6 = Exercise(
        id="6",
        name="Zancadas",
        description="20 repeticiones",
        img="",
    )
    exercise7 = Exercise(
        id="7",
        name="Hip-thrust",
        description="20 repeticiones",
        img="",
    )
    exercise8 = Exercise(
        id="8",
        name="Patadas de burro",
        description="20 segundos",
        img="",
    )
    exercise9 = Exercise(
        id="9",
        name="Hip-thrust",
        description="20 repeticiones",
        img="",
    )

    exercise0 = Exercise(
        id="0",
        name="Sentadillas",
        description="10 repeticiones",
        img="",
    )

    exercise1 = Exercise(
        id="1",
        name="Patadas de burro",
        description="10 repeticiones",
        img="",
    )

    exercise2 = Exercise(
        id="2",
        name="Hip-thrust",
        description="10 repeticiones",
        img="",
    )

    exercise3 = Exercise(
        id="3",
        name="Zancadas",
        description="10 repeticionesa",
        img="",
    )

    exercise4 = Exercise(
        id="4",
        name="Hip-thrust",
        description="10 repeticiones",
        img="",
    )
    exercises_repository.save(exercise0)
    exercises_repository.save(exercise1)
    exercises_repository.save(exercise2)
    exercises_repository.save(exercise3)
    exercises_repository.save(exercise4)
    exercises_repository.save(exercise5)
    exercises_repository.save(exercise6)
    exercises_repository.save(exercise7)
    exercises_repository.save(exercise8)
    exercises_repository.save(exercise9)


main()
