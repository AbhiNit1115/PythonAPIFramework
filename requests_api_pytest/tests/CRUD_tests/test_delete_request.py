from requests_api_pytest.common.api_request.request_methods import RequestAPI
from requests_api_pytest.common.api_response.response_confirmation import ResponseValidation


def test_request_to_delete_users_204_status_code(url_configuration, rp_logger):

    url_configuration.end_point = "api/users/2"
    response = RequestAPI.requests_delete(url_configuration)
    ResponseValidation.validate_status_code(response, 204)


def test_request_to_delete_users_200_status_code(url_configuration2, rp_logger):
    rp_logger.info("Sample test method - CSV Parsing for response body1")
    url_configuration2.end_point = "api/v1/Activities/1"
    response = RequestAPI.requests_delete(url_configuration2)
    ResponseValidation.validate_status_code(response, 200)
