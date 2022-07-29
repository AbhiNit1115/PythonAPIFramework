import pytest
from requests_api_pytest.common.api_request.request_methods import RequestAPI
from requests_api_pytest.common.api_response.response_confirmation import ResponseValidation
from requests_api_pytest.common.api_response.desconstruct_response import deserialize


@pytest.mark.first
def test_get_request_to_list_users(url_configuration):
    url_configuration.end_point = "api/users/2"
    response = RequestAPI.requests_get(url_configuration)
    ResponseValidation.validate_status_code(response, 200)
    print(response.content)
    des_resp = deserialize(response, url_configuration.content_type)
    assert (des_resp['data']['id']) == 2, "Assertion Error"


@pytest.mark.second
def test_get_request_user_not_found(url_configuration):
    url_configuration.end_point = "api/users/23"
    response = RequestAPI.requests_get(url_configuration)
    ResponseValidation.validate_status_code(response, 404)
    ResponseValidation.get_status_code(response)


@pytest.mark.third
def test_get_request_delayed_response(url_configuration):
    url_configuration.end_point = "api/users?delay=9"
    response = RequestAPI.requests_get(url_configuration)
    print(response.url)
    ResponseValidation.validate_status_code(response, 200)
    ResponseValidation.get_status_code(response)


@pytest.mark.fourth
def test_get_request_with_basic_auth(url_configuration3):
    url_configuration3.end_point = "basic-auth/user/passwd"
    url_configuration3.auth = ('user', 'passwd')
    response = RequestAPI.requests_get(url_configuration3)
    ResponseValidation.validate_status_code(response, 200)


@pytest.mark.fifth
def test_get_request_with_bearer_auth(url_configuration3):
    url_configuration3.end_point = "bearer"
    url_configuration3.headers["Authorization"] = "Bearer {token}"
    response = RequestAPI.requests_get(url_configuration3)
    ResponseValidation.validate_status_code(response, 200)
    ResponseValidation.get_status_code(response)


@pytest.mark.sixth
def test_get_request_with_digest_auth(url_configuration3):
    url_configuration3.end_point = "digest-auth/auth/user/pass"
    url_configuration3.include_digest_authentication('user', 'pass')
    response = RequestAPI.requests_get(url_configuration3)
    ResponseValidation.validate_status_code(response, 200)
