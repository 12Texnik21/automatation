import pytest
import requests
import json

X_client_URL = "https://x-clients-be.onrender.com"

path = '/employee/'
@pytest.fixture()

def get_token(username='raphael', password='cool-but-crude'):
    log_pass = {'username':username,'password':password}
    resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
 


class Company:
    def __init__(self, url = X_client_URL):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company',headers=headers, params=body)
        return response.json()
    
    def last_active_company_id(self):
        active_params = {'active':'true'}
        response = requests.get(
            self.url + '/company', params=active_params)
        return response.json()[-1]['id']
    
class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url

    def get_list(self, company_id: int):
        company = {'company':company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    def add_new(self, token: str, body: json):
        headers ={'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json() 
    
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response
    
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token':token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers,
        json=body)
        return response


employer = Employer(X_client_URL)
company = Company(X_client_URL)
X_client_URL = "https://x-clients-be.onrender.com"

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'firstName':'Ivan',
        'lastName':'Petrov',
        'middleName':'srting',
        'companyId':com_id,
        'email':'test@mail.ru',
        'url':'string',
        'phone':'string',
        'birtdate':"2024-05-16T11:02:45.622Z",
        'isActive':'true'
    }

    new_employer_id = (employer.add_new(token, body_employer))['id']
    
    assert new_employer_id is not None

    assert str(new_employer_id).isdigit()

    info = employer.get_info(new_employer_id)

    assert info.json()['id'] == new_employer_id

    assert info.status_code == 200

def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
        'id': 0,
        'firstName':'Ivan',
        'lastName':'Petrov',
        'middleName':'srting',
        'companyId':com_id,
        'email':'test@mail.ru',
        'url':'string',
        'phone':'string',
        'birtdate':"2024-05-16T11:02:45.622Z",
        'isActive':'true'
    }
    new_employer = employer.add_new(token, body_employer)
    
    assert new_employer['message'] == 'Unauthorized'

def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_emloyer = {}

    new_employer = employer.add_new(token, body_emloyer)
    
    assert new_employer['message'] == 'Internal server error'

def test_get_employer():
    com_id = company.last_active_company_id()

    list_employers = employer.get_list(com_id)

    assert isinstance(list_employers, list)

def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
         
def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
