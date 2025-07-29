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


# тест создания проекта с названием 'python1'
def test_create_project(get_company_id):
    company_id = get_company_id
    token = get_token(company_id)
    user_id = get_user_id(token)
    project_data = {
        'title': 'python1',
        'users': {
            user_id: 'admin'
        }
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    resp = requests.post(DataAuth.base_url + '/projects',
                         json=project_data, headers=headers)
    assert resp.status_code == 201
