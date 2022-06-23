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

    exercise1 = Exercise(
        id=1,
        name="Sentadillas",
        description="10 repeticiones",
        img="",
        category="pierna",
    )
    exercise2 = Exercise(
        id=2,
        name="Hip thrust",
        description="10 repeticiones",
        img="",
        category="pierna",
    )
    exercise3 = Exercise(
        id=3,
        name="Patadas de gluteo",
        description="10 repeticiones con cada pierna",
        img="",
        category="pierna",
    )
    exercise4 = Exercise(
        id=4,
        name="Peso muerto",
        description="15 repeticiones",
        img="",
        category="pierna",
    )
    exercise5 = Exercise(
        id=5,
        name="Hip thrust",
        description="10 repeticiones",
        img="",
        category="pierna",
    )

    exercise6 = Exercise(
        id=6,
        name="Plancha",
        description="30 segundos",
        img="",
        category="abdomen",
    )

    exercise7 = Exercise(
        id=7,
        name="Abdominales",
        description="15 repeticiones",
        img="",
        category="abdomen",
    )

    exercise8 = Exercise(
        id=8,
        name="Dead bug",
        description="15 repeticiones",
        img="",
        category="abdomen",
    )

    exercise9 = Exercise(
        id=9,
        name="Bicycle crunches",
        description="15 repeticionesa",
        img="",
        category="abdomen",
    )

    exercise10 = Exercise(
        id=10,
        name="Giros rusos",
        description="15 repeticiones",
        img="",
        category="abdomen",
    )

    exercise11 = Exercise(
        id=11,
        name="Curl de bíceps",
        description="15 repeticiones",
        img="",
        category="brazos",
    )

    exercise12 = Exercise(
        id=12,
        name="Flexiones",
        description="10 repeticiones",
        img="",
        category="brazos",
    )

    exercise13 = Exercise(
        id=13,
        name="Levantamientos laterales",
        description="15 repeticiones",
        img="",
        category="brazos",
    )

    exercise14 = Exercise(
        id=14,
        name="Rotaciones externa",
        description="15 repeticiones",
        img="",
        category="brazos",
    )
    exercise15 = Exercise(
        id=15,
        name="Remo",
        description="10 repeticiones",
        img="",
        category="brazos",
    )

    exercise16 = Exercise(
        id=16,
        name="Correr",
        description="20 minutos",
        img="",
        category="hit",
    )
    exercise17 = Exercise(
        id=17,
        name="Zancadas",
        description="15 repeticiones",
        img="",
        category="hit",
    )
    exercise18 = Exercise(
        id=18,
        name="Jumping Jacks",
        description="15 repeticiones",
        img="",
        category="hit",
    )
    exercise19 = Exercise(
        id=19,
        name="Burpees ",
        description="10 repeticiones",
        img="",
        category="hit",
    )

    exercise20 = Exercise(
        id=20,
        name="Mountain Climbers",
        description="20 repeticiones",
        img="",
        category="hit",
    )

    exercise21 = Exercise(
        id=21,
        name="Sentadillas",
        description="20 repeticiones",
        img="",
        category="pierna",
    )
    exercise22 = Exercise(
        id=22,
        name="Hip thrust",
        description="20 repeticiones",
        img="",
        category="pierna",
    )
    exercise23 = Exercise(
        id=23,
        name="Patadas de gluteo",
        description="25 repeticiones con cada pierna",
        img="",
        category="pierna",
    )
    exercise24 = Exercise(
        id=24,
        name="Peso muerto",
        description="15 repeticiones",
        img="",
        category="pierna",
    )
    exercise25 = Exercise(
        id=25,
        name="Hip thrust",
        description="20 repeticiones",
        img="",
        category="pierna",
    )

    exercise26 = Exercise(
        id=26,
        name="Plancha",
        description="30 segundos",
        img="",
        category="abdomen",
    )

    exercise27 = Exercise(
        id=27,
        name="Abdominales",
        description="25 repeticiones",
        img="",
        category="abdomen",
    )

    exercise28 = Exercise(
        id=28,
        name="Dead bug",
        description="25 repeticiones",
        img="",
        category="abdomen",
    )

    exercise29 = Exercise(
        id=29,
        name="Bicycle crunches",
        description="30 repeticionesa",
        img="",
        category="abdomen",
    )

    exercise30 = Exercise(
        id=30,
        name="Giros rusos",
        description="20 repeticiones",
        img="",
        category="abdomen",
    )

    exercise31 = Exercise(
        id=31,
        name="Curl de bíceps",
        description="20 repeticiones",
        img="",
        category="brazos",
    )

    exercise32 = Exercise(
        id=32,
        name="Flexiones",
        description="15 repeticiones",
        img="",
        category="brazos",
    )

    exercise33 = Exercise(
        id=33,
        name="Levantamientos laterales",
        description="20 repeticiones",
        img="",
        category="brazos",
    )

    exercise34 = Exercise(
        id=34,
        name="Rotaciones externa",
        description="20 repeticiones",
        img="",
        category="brazos",
    )
    exercise35 = Exercise(
        id=35,
        name="Remo",
        description="25 repeticiones",
        img="",
        category="brazos",
    )

    exercise36 = Exercise(
        id=36,
        name="Correr",
        description="30 minutos",
        img="",
        category="hit",
    )
    exercise37 = Exercise(
        id=37,
        name="Zancadas",
        description="25 repeticiones",
        img="",
        category="hit",
    )
    exercise38 = Exercise(
        id=38,
        name="Jumping Jacks",
        description="20 repeticiones",
        img="",
        category="hit",
    )
    exercise39 = Exercise(
        id=39,
        name="Burpees",
        description="20 repeticiones",
        img="",
        category="hit",
    )

    exercise40 = Exercise(
        id=40,
        name="Mountain Climbers",
        description="25 repeticiones",
        img="",
        category="hit",
    )

    exercises_repository.save(exercise1)
    exercises_repository.save(exercise2)
    exercises_repository.save(exercise3)
    exercises_repository.save(exercise4)
    exercises_repository.save(exercise5)
    exercises_repository.save(exercise6)
    exercises_repository.save(exercise7)
    exercises_repository.save(exercise8)
    exercises_repository.save(exercise9)
    exercises_repository.save(exercise10)
    exercises_repository.save(exercise11)
    exercises_repository.save(exercise14)
    exercises_repository.save(exercise12)
    exercises_repository.save(exercise15)
    exercises_repository.save(exercise16)
    exercises_repository.save(exercise17)
    exercises_repository.save(exercise18)
    exercises_repository.save(exercise19)
    exercises_repository.save(exercise20)
    exercises_repository.save(exercise21)
    exercises_repository.save(exercise13)
    exercises_repository.save(exercise22)
    exercises_repository.save(exercise23)
    exercises_repository.save(exercise24)
    exercises_repository.save(exercise25)
    exercises_repository.save(exercise26)
    exercises_repository.save(exercise27)
    exercises_repository.save(exercise28)
    exercises_repository.save(exercise29)
    exercises_repository.save(exercise30)
    exercises_repository.save(exercise31)
    exercises_repository.save(exercise32)
    exercises_repository.save(exercise33)
    exercises_repository.save(exercise34)
    exercises_repository.save(exercise35)
    exercises_repository.save(exercise36)
    exercises_repository.save(exercise37)
    exercises_repository.save(exercise38)
    exercises_repository.save(exercise39)
    exercises_repository.save(exercise40)


main()
