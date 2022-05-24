# from src.lib.utils import temp_file

# from src.webserver import create_app
# from src.domain.user import User, UserRepository


# def test_should_return_data_from_new_user():
#     users_repository = UserRepository(temp_file())
#     app = create_app(repositories={"users": users_repository})
#     client = app.test_client()

#     body = {
#         "id": "user-form-1",
#         "user_id": "uu1",
#         "goal": "gain_weight",
#         "weight": "70",
#         "height": "185",
#         "experiencie": 1,
#     }
#     response_post = client.post(
#         "/api/users", json=body, headers={"Authorization": "uu1"}
#     )

#     assert response_post.status_code == 200

#     response_get = client.get("/api/users", headers={"Authorization": "uu1"})

#     user = response_get.json
#     assert user[0]["id"] == "uu1"
#     assert user[0]["user_id"] == "christian"
#     assert user[0]["goal"] == "gain_weight"
#     assert user[0]["weight"] == "70"
#     assert user[0]["height"] == "185"
#     assert user[0]["experiencie"] == 1
