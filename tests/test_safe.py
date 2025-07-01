import pytest
from api.user_api import UserAPi
from api.schema import *


@pytest.mark.safe
def test_get_users_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_all_users(2)
    assert response.status_code == 200

@pytest.mark.safe
def test_get_users(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_all_users(2).json()
    assert UsersListSchema(**response)

@pytest.mark.safe
def test_get_users_by_id_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_user_by_id(1)
    assert response.status_code == 200

@pytest.mark.safe
def test_get_users_by_id(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_user_by_id(1).json()
    assert SingleUser(**response)

@pytest.mark.safe
def test_user_not_foud(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_user_by_id(23)
    assert response.status_code == 404

@pytest.mark.safe
def test_resources_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_all_resources()
    assert response.status_code == 200

@pytest.mark.safe
def test_resources(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_all_resources()
    assert ResourceListSchema(**response.json())

@pytest.mark.safe
def test_one_resource(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_resource_by_id(1)
    print(response.json())
    assert SingleResource(**response.json())

@pytest.mark.safe
def test_unknown_id(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.get_resource_by_id(23)
    assert response.status_code == 404

