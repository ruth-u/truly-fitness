from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.user import User, UserRepository


def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    christian = User(
        id="uu1", full_name="Christian Garcia", user_name="chris11", password="chris123"
    )
    user_repository.save(christian)

    return client


def test_should_validate_login():
    client = setup()

    body = {"user_name": "chris11", "password": "chris123"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 200
    response_get = client.get("/api/users")

    user = response_get.json
    assert user[0]["user_name"] == "chris11"
    assert user[0]["password"] == "chris123"


# def test_should_fail_if_invalid_password():
#     client = setup()

#     body = {"user": "user-tomas", "password": "el peor"}
#     response = client.post("/auth/login", json=body)

#     assert response.status_code == 401


# def test_should_fail_if_user_not_exists():
#     client = setup()

#     body = {"user": "user-not-exists", "password": "el mediano"}
#     response = client.post("/auth/login", json=body)

#     assert response.status_code == 401
