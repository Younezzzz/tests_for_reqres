import pytest
from api.user_api import UserAPi


@pytest.mark.usefixtures("headers")
@pytest.mark.api
def test_get_users_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_all_users()
    assert response.status_code == 200

@pytest.mark.usefixtures("headers")
def test_get_users_by_id_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_user_by_id(1)
    assert response.status_code == 200

@pytest.mark.usefixtures("headers")
def test_create_user_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.new_user({"job":"Chlenosos","name":"Ayan"})
    assert response.status_code == 201