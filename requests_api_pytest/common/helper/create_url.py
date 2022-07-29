from urllib.parse import urljoin
import json


def make_url(config):
    if config.base_url:
        final_url = urljoin(config.base_url, config.end_point)
    return final_url


def rest_response_handle(response):
    return response, response.status_code, response.text, response.json()


def json_converter(data):
    json_string = json.dumps(data)
    return json_string
