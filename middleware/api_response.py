from typing import List

from middleware.api_error import ApiError


class ApiResponse:
    data: object
    errors: List[ApiError]

    def __init__(self, data: object, errors: List[ApiError]):
        self.data = data
        self.errors = errors
