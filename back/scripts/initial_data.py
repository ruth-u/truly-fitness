import sys

sys.path.insert(0, "")


def main():

    from src.domain.user import User, UserRepository

    database_path = "data/database.db"
    users_repository = UserRepository(database_path)

    christian = User(
        id="uu1", full_name="Christian Garcia", user_name="chris11", password="chris123"
    )
    nagore = User(
        id="uu2", full_name="Nagore Cuevas", user_name="nagore.c", password="nagore123"
    )

    users_repository.save(christian)
    users_repository.save(nagore)


main()
