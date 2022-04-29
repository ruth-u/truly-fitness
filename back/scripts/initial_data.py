import sys

sys.path.insert(0, "")


def main():

    from src.domain.users import User, UserRepository

    database_path = "data/database.db"
    users_repository = UserRepository(database_path)

    christian = User(
        id="uu1", user_name="christian", weight="110", height="185", experiencie=0
    )

    users_repository = UserRepository(database_path)
    users_repository.save(christian)

    nagore = User(
        id="uu1", user_name="nagore", weight="50", height="165", experiencie=1
    )

    users_repository = UserRepository(database_path)
    users_repository.save(nagore)


main()
