import pytest
from requests_api_pytest.common.api_request.request_methods import RequestAPI
from requests_api_pytest.common.api_response.desconstruct_response import deserialize
from requests_api_pytest.common.api_response.response_confirmation import ResponseValidation


@pytest.mark.first
def test_verify_record_update_and_status_code(url_configuration3):
    url_configuration3.end_point = "put"
    response = RequestAPI.requests_put(url_configuration3)
    ResponseValidation.validate_status_code(response, 200)


@pytest.mark.second
def test_validate_put_with_json_response(url_configuration):
    url_configuration.end_point = "api/users/2"
    url_configuration.headers = {'Content-Type': 'application/json'}
    request_data = RequestAPI.open_json_file('../test_data/update_user_details.json', 'r')
    response = RequestAPI.requests_put(url_configuration, json_data=request_data)
    des_resp = deserialize(response, url_configuration.headers['Content-Type'])
    assert des_resp['name'] == 'James Watt', "Assertion error"


@pytest.mark.third
def test_get_resp(url_configuration3):
    url_configuration3.end_point = "basic-auth"
    response = RequestAPI.requests_get(url_configuration3)
    print(response.status_code)

