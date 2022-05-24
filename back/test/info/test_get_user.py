from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.user import User, UserRepository


def test_should_return_empty_list_of_users():

    users_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_return_a_user():
    users_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()

    christian = User(
        id="uu1",
        full_name="christian garcia",
        user_name="christian",
        password="chris123",
    )
    users_repository.save(christian)

    jeff = User(
        id="uu2",
        full_name="jefferson sanchez",
        user_name="jeff",
        password="jeff123",
    )
    users_repository.save(jeff)

    response = client.get("/api/users")
    assert response.json == [
        {
            "id": "uu1",
            "full_name": "christian garcia",
            "user_name": "christian",
            "password": "chris123",
        },
        {
            "id": "uu2",
            "full_name": "jefferson sanchez",
            "user_name": "jeff",
            "password": "jeff123",
        },
    ]
