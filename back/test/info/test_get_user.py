from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.users import User, UserRepository


def test_should_return_empty_list_of_users():

    users_repository = UserRepository(temp_file())
    app = create_app(repositories={"user": users_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_return_a_user():
    users_repository = UserRepository(temp_file())
    app = create_app(repositories={"user": users_repository})
    client = app.test_client()

    christian = User(
        id="uu1", user_name="christian", weight="110", height="185", experiencie=1
    )
    users_repository.save(christian)

    response = client.get("/api/users")
    assert response.json == [
        {
            "id": "uu1",
            "user_name": "christian",
            "weight": "110",
            "height": "185",
            "experiencie": 1,
        }
    ]
