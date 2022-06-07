from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.user import User, UserRepository


def test_should_return_data_from_new_user():
    users_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": users_repository})
    client = app.test_client()

    body = {
        "id": "uu1",
        "first_name": "Christian",
        "last_name": "Garcia",
        "user_name": "chris11",
        "password": "chris123",
        "goal": "ganar peso",
        "weight": "70",
        "height": "185",
        "experiencie": 1,
    }
    response_post = client.post(
        "/api/users", json=body, headers={"Authorization": "uu1"}
    )

    assert response_post.status_code == 200

    response_get = client.get("/api/users", headers={"Authorization": "uu1"})

    user_list = response_get.json
    assert user_list[0]["id"] == "uu1"
    assert user_list[0]["first_name"] == "Christian"
    assert user_list[0]["last_name"] == "Garcia"
    assert user_list[0]["user_name"] == "chris11"
    assert user_list[0]["password"] == "chris123"
    assert user_list[0]["goal"] == "ganar peso"
    assert user_list[0]["weight"] == "70"
    assert user_list[0]["height"] == "185"
    assert user_list[0]["experiencie"] == 1
