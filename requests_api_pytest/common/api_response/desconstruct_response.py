import json
from jsonpath_ng import parse


def deserialize(response, content_type):
    deserialize_data = _get_parsed_data(content_type)
    return deserialize_data(response)


def _get_parsed_data(content_type):
    if content_type.lower() == 'application/json':
        return _json_parsed_data
    else:
        raise ValueError(f'Incorrect content type : {content_type} provided')


def _json_parsed_data(response):
    return json.loads(response.content)


def _json_parsed_data1(response):
    json_response = json.loads(response.text)
    return json_response


class JSONValidator:
    """
        JSON Validator/Utility class to validate the json api_response body with expected json nodes/values
    """

    @staticmethod
    def validate_node_in_response_body(json_data, node, expected_value=None):
        if node in json_data:
            assert True
            if expected_value is not None:
                actual_value = json_data[node]
                assert actual_value == expected_value, f"Expected value for {node} is {expected_value} is not " \
                                                       f"matching with actual value{actual_value} "
        else:
            assert False, f"{node} not exists"

    @staticmethod
    def validate_node_with_jsonpath_response(json_data, json_path, expected_value):
        json_path_expr = parse(json_path)
        match = json_path_expr.find(json_data)
        assert match[0].value == expected_value, f"Expected value {expected_value} does not match with actual value"
