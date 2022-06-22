from atexit import register
from src.lib.utils import temp_file, object_to_json

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
        user_name="christian",
        password="chris123",
        first_name="christian",
        last_name="garcia",
        goal="ganar peso",
        weight="70",
        height="185",
        experiencie=1,
        register_date="2022-06-07",
    )
    users_repository.save(christian)

    jeff = User(
        id="uu2",
        user_name="jeff",
        password="jeff123",
        first_name="jefferson",
        last_name="sanchez",
        goal="perder peso",
        weight="110",
        height="175",
        experiencie=0,
        register_date="2022-06-08",
    )
    users_repository.save(jeff)

    response = client.get("/api/users")

    user_list = response.json
    assert len(user_list) == 2
    assert user_list[0]["id"] == "uu1"
    assert user_list[0]["user_name"] == "christian"
    assert user_list[0]["password"] == "chris123"
    assert user_list[0]["goal"] == "ganar peso"
    assert user_list[0]["weight"] == "70"
    assert user_list[0]["height"] == "185"
    assert user_list[0]["experiencie"] == 1
    assert user_list[1]["id"] == "uu2"
    assert user_list[1]["user_name"] == "jeff"
    assert user_list[1]["password"] == "jeff123"
    assert user_list[1]["goal"] == "perder peso"
    assert user_list[1]["weight"] == "110"
    assert user_list[1]["height"] == "175"
    assert user_list[1]["experiencie"] == 0
