class URLResponse:

    def __init__(self, response, status_code, text, json_response, error_msg, json_error_msg):
        self.status_code = status_code
        self.text = text
        self.json_response = json_response
        self.http_error_msg = error_msg
        self.response = response
        self.json_error_msg = json_error_msg


class ResponseValidation:

    @staticmethod
    def validate_response_schema(response):
        return response.url.startswith("https:")

    @staticmethod
    def get_status_code(response):
        return response.status_code

    @staticmethod
    def get_body_content(response):
        print(response.content)

    @staticmethod
    def get_body_json(response):
        print(response.json())

    @staticmethod
    def validate_status_code(response, expected_status_code):
        actual_status_code = response.status_code
        print("Status Code is - ", response.status_code)
        assert actual_status_code == expected_status_code, f"Actual Status code {actual_status_code} is not matching " \
                                                           f"with expected status code: {expected_status_code}. "
