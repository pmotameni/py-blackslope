import pytest
from pydantic import BaseModel, ValidationError
from rest_framework.test import APIRequestFactory

from apiapp.common.decorators.strong_type import strong_type
from apiapp.operations.movies import MovieController
from apiapp.services.movies import Movie as MovieDomainModel
from apiapp.services.movies import MovieService


@pytest.fixture(scope="function")
def factory():
    return APIRequestFactory()


class TestStrongTypeDecoratorShould:
    """Tests for Movies Controller get  which returns multiple movies"""

    def test_fills_strong_type(self, factory, mocker):
        class TestRequest:
            data: any

        class TestType(BaseModel):
            test: str

        @strong_type(request_position=0)
        def test(request, model: TestType):
            assert model is not None and type(model) is TestType

        test_request = TestRequest()
        test_request.data = {"test": "something"}

        test(test_request)
