import jsonpickle
from django.http import HttpResponse

from middleware.api_exception import ApiException
from middleware.api_http_status_code import ApiHttpStatusCode
from middleware.api_response import ApiResponse


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        response: ApiResponse
        status_code = ApiHttpStatusCode.InternalServerError
        if type(exception) is ApiException:
            api_exception: ApiException = exception
            status_code = api_exception.api_http_status_code
            response = ApiResponse(api_exception.data, api_exception.errors)
        else:
            response = ApiResponse(None, status_code.description)

        # TODO: log

        return HttpResponse(status=status_code.value,
                            reason=jsonpickle.encode(response),
                            content_type="application/json")
