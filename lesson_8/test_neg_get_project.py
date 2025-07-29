import requests
import pytest
from config import DataAuth


@pytest.fixture
# получение id компании
def get_company_id():

    company_data = {
        'login': DataAuth.login,
        'password': DataAuth.password,
        'name': DataAuth.name
    }
    resp = requests.post(DataAuth.base_url + '/auth/companies',
                         json=company_data)
    company_id = resp.json()['content'][0]["id"]
    return company_id


# получение списка ключей и выбор первого ключа
def get_token(company_id):
    auth_data = {
        'login': DataAuth.login,
        'password': DataAuth.password,
        'companyId': company_id
    }
    resp = requests.post(DataAuth.base_url + '/auth/keys/get', json=auth_data)
    token = resp.json()[0]['key']
    return token


# получение id пользователя
def get_user_id(token):
    my_headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(DataAuth.base_url + '/users', headers=my_headers)
    user_id = resp.json()['content'][0]["id"]
    return user_id


# получение id проектов и выбор id последнего проекта
def get_project_id(company_id):
    token = get_token(company_id)
    headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(DataAuth.base_url + '/projects', headers=headers)
    project_id = resp.json()['content'][-1]["id"]
    return project_id


# тест получения проекта по id с неверным токеном
def test_get_project(get_company_id):
    company_id = get_company_id
    token = 123  # неверный токен '123'
    project_id = get_project_id(company_id)
    headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.get(f"{DataAuth.base_url}/projects/{project_id}",
                        headers=headers)
    assert resp.status_code == 401
