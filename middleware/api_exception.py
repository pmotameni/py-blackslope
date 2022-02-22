from typing import List
from middleware.api_error import ApiError
from middleware.api_http_status_code import ApiHttpStatusCode


class ApiException(Exception):
    api_http_status_code: ApiHttpStatusCode
    errors: List[ApiError]
    data: object

    def __init__(self, api_http_status_code: ApiHttpStatusCode, errors: List[ApiError], data: object = None):
        self.api_http_status_code = api_http_status_code
        self.errors = errors
        self.data = data

