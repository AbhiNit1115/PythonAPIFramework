import json
import requests
from requests_api_pytest.common.api_request.requests_config import RestAPIConfig
from requests_api_pytest.common.helper.create_url import make_url, rest_response_handle


class RequestAPI:

    @staticmethod
    def requests_get(config: RestAPIConfig):
        url = make_url(config)
        response = requests.get(url=url, headers=config.headers, timeout=config.time_out, params=config.params,
                                auth=config.auth)
        response, status_code, text, json = rest_response_handle(response)
        return response

    @staticmethod
    def requests_post(config: RestAPIConfig, json_data=None):
        url = make_url(config)
        response = requests.post(url=url, params=config.params,
                                 json=json_data,
                                 headers=config.headers,
                                 timeout=config.time_out,
                                 allow_redirects=config.allow_redirects,
                                 auth=config.auth)
        response, status_code, text, json = rest_response_handle(response)
        return response

    @staticmethod
    def requests_put(config: RestAPIConfig, json_data=None):
        url = make_url(config)
        response = requests.put(url=url, params=config.params,
                                json=json_data,
                                headers=config.headers,
                                timeout=config.time_out,
                                allow_redirects=config.allow_redirects,
                                auth=config.auth)
        response, status_code, text, json = rest_response_handle(response)
        return response

    @staticmethod
    def requests_delete(config: RestAPIConfig, json_data=None):
        url = make_url(config)
        response = requests.delete(url=url,
                                   headers=config.headers,
                                   params=config.params,
                                   data=json_data,
                                   timeout=config.time_out,
                                   auth=config.auth
                                   )

        return response

    @staticmethod
    def open_json_file(filename, mode):
        data_file = open(filename, mode)
        request_json = json.loads(data_file.read())
        return request_json
