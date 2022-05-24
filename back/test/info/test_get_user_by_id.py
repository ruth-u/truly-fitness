# from src.lib.utils import temp_file

# from src.webserver import create_app
# from src.domain.users import User, UserRepository


# def test_should_return_existing_user_by_id():

#     users_repository = UserRepository(temp_file())
#     app = create_app(repositories={"users": users_repository})
#     client = app.test_client()

#     christian = {
#         "id": "user-1",
#         "user_name": "christian",
#         "weight": "120",
#         "height": "185",
#         "experiencie": 1,
#     }

#     nagore = {
#         "id": "user-2",
#         "user_name": "nagore",
#         "weight": "160",
#         "height": "48",
#         "experiencie": 0,
#     }

#     response_christian = client.get(
#         "/api/users/user-1", json=christian, headers={"Authorization": "user-1"}
#     )
#     response_nagore = client.get(
#         "/api/users/user-2", json=nagore, headers={"Authorization": "user-2"}
#     )

#     # ASSERT (then)
#     assert response_christian.status_code == 200
#     christian = response_christian.json
#     assert christian["id"] == "user-1"
#     assert christian["user_name"] == "christian"
#     assert christian["weight"] == "120"
#     assert christian["height"] == "185"
#     assert christian["experiencie"] == 1

#     assert response_nagore.status_code == 200
#     nagore = response_nagore.json
#     assert nagore["id"] == "user-2"
#     assert nagore["user_name"] == "nagore"
#     assert nagore["weight"] == "160"
#     assert nagore["height"] == "48"
#     assert nagore["experiencie"] == 0
