import json
import requests

import pytest
from requests_api_pytest.common.api_request.request_methods import RequestAPI
from requests_api_pytest.common.api_response.desconstruct_response import deserialize
from requests_api_pytest.common.api_response.response_confirmation import ResponseValidation


@pytest.mark.first
def test_post_with_json_none_json_response(url_configuration):
    url_configuration.end_point = "api/users"
    url_configuration.headers = {'Content-Type': 'application/json'}
    request_data = RequestAPI.open_json_file('../test_data/user_details.json', 'r')
    response = RequestAPI.requests_post(url_configuration, json_data=request_data)
    des_resp = deserialize(response, url_configuration.headers['Content-Type'])
    assert des_resp['name'] == 'Abhi', "Assertion error"


@pytest.mark.first
def test_post_with_json_none_json_response(add: str, remove: str):
    request = "https://jira.lgi.io/rest/raven/1.0/api/testplan/TERRA-55752/testexecutionn"
    values = {"add": [add], "remove": [remove]}
    if values:
        values = json.dumps(values)

    response = RequestAPI.requests_post(request, json_data=values)
    if response.status_code == 200:
        return json.loads(response.text)
    raise AssertionError(response.text)
    return self.send_post_request(request, values=values)


@pytest.mark.second
def test_post_data_validate_status_code_201(url_configuration):
    url_configuration.end_point = "api/users"
    url_configuration.headers = {'Content-Type': 'application/json'}
    request_data = RequestAPI.open_json_file('../test_data/user_details.json', 'r')
    response = RequestAPI.requests_post(url_configuration, json_data=request_data)
    print(response.url)
    ResponseValidation.validate_status_code(response, 201)


@pytest.mark.third
def test_post_data_validate_successful_registration(url_configuration):
    url_configuration.end_point = "api/register"
    url_configuration.headers = {'Content-Type': 'application/json'}
    request_data = RequestAPI.open_json_file('../test_data/register_success.json', 'r')
    response = RequestAPI.requests_post(url_configuration, json_data=request_data)
    ResponseValidation.validate_status_code(response, 200)
    des_resp = deserialize(response, url_configuration.headers['Content-Type'])
    assert des_resp['id'] == 4, AssertionError
