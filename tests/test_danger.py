import pytest
from api.user_api import UserAPi
from api.schema import *

@pytest.mark.danger
def test_create_user_status_code(api_url, headers):
    api = UserAPi(api_url, header=headers)
    response = api.new_user({"job":"Chlenosos","name":"Ayan"})
    assert response.status_code == 201

@pytest.mark.danger
def test_create_user(api_url, headers):
    api = UserAPi(api_url, headers)
    response = api.new_user({"job":"krutoi_qa_prosto_legenda","name":"Vasya"}).json()
    assert UserSchema(**response)

@pytest.mark.danger
def test_update_job_user(api_url, headers):
    api = UserAPi(api_url, headers)
    response = api.update_user(2,'Ayan','bedolaga')
    assert response.json()['name'] == 'Ayan' and response.json()['job'] == 'bedolaga'