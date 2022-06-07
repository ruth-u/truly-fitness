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
    )

    users_repository.save(christian)
    users_repository.save(nagore)

    from src.domain.exercises import Exercise, ExerciseRepository

    database_path = "data/database.db"
    exercises_repository = ExerciseRepository(database_path)

    exercise5 = Exercise(
        id="005",
        name="Sentadillas",
        description="20 repeticiones",
        img="",
        week_day="8",
        week="2",
    )
    exercise6 = Exercise(
        id="006",
        name="Zancadas",
        description="20 repeticiones",
        img="",
        week_day="8",
        week="2",
    )
    exercise7 = Exercise(
        id="007",
        name="Hip-thrust",
        description="20 repeticiones",
        img="",
        week_day="8",
        week="2",
    )
    exercise8 = Exercise(
        id="008",
        name="Patadas de burro",
        description="20 segundos",
        img="",
        week_day="8",
        week="2",
    )
    exercise9 = Exercise(
        id="009",
        name="Hip-thrust",
        description="20 repeticiones",
        img="",
        week_day="8",
        week="2",
    )

    exercise0 = Exercise(
        id="000",
        name="Sentadillas",
        description="10 repeticiones",
        img="",
        week_day="1",
        week="1",
    )

    exercise1 = Exercise(
        id="001",
        name="Patadas de burro",
        description="10 repeticiones",
        img="",
        week_day="1",
        week="1",
    )

    exercise2 = Exercise(
        id="002",
        name="Hip-thrust",
        description="10 repeticiones",
        img="",
        week_day="1",
        week="1",
    )

    exercise3 = Exercise(
        id="003",
        name="Zancadas",
        description="10 repeticionesa",
        img="",
        week_day="1",
        week="1",
    )

    exercise4 = Exercise(
        id="004",
        name="Hip-thrust",
        description="10 repeticiones",
        img="",
        week_day="1",
        week="1",
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
