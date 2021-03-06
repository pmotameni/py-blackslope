# py-blackslope

Blackslope is a reference architecture for implementing the API layer for web applications. It contains a set of guidelines and best practices.
The py-blackslope is a python implementation of Blackslope. The underlying framework for this implementation is [Django](https://www.djangoproject.com/) and [Django REST](https://www.django-rest-framework.org/) framework

## Other BlackSlope Implementations

-   [BlackSlope.NET](https://github.com/SlalomBuild/blackslope.net) is the .NET implementation of the BlackSlope.

# How to run
## Python
Current py-blackslope uses [Python 3.10](https://www.python.org/downloads/release/python-3100/).
## Poetry 
[Poetry](https://python-poetry.org/docs/) is the preferred tool for dependency management for py-blackslope.

## Install dependencies and pre-commit git hooks

```shell
$ poetry run install
```

## Initialize the environment

For local environment a ".env" file should be created under the blackslope folder. This file contains the secretes for local use. For CI/CD pipeline refer to the user guide of the tool to create environment variables.

```local.env
# Do not check it the .env files which contain secrets
SECRET_KEY=<some_random_secret>
DEBUG=True
LOG_HANDLERS='["file", "console"]'
```

## Run using poetry script

```shell
$ poetry run start
```

## Run using shell script

```shell
$ ./run.sh
```

## Manual run

```shell
$ poetry run python manage.py runserver
```

## Run tests and get coverage

To run tests

```shell
$ poetry run pytest
```

To include coverage in the result

```shell
$ poetry run pytest --cov
```

## Linting

To lint the application

```shell
poetry run lint
```

This command will lint your application and fix what it can.

## Pre-commit

When you try to commit your code in git, the pre-commit package will run linting and tests against your application. These checks help ensure code consistency and quality. Any failures will prevent you from committing your code. To check if pre-commit will fail without committing, run the following command:

```shell
poetry run pre-commit
```

# How to add API Endpoint

Py-BlackSlope uses the View Class approach for API endpoints. To add new endpoints create a folder under the `operations` and name it according to the resource. Add a file name `views.py` and in the file add the class which serve as controllers. Each method in a controller will handle a HTTP method.

Add the Paths to the API in:
the `urls.py` under the `apiapp` folder

-   import the function that handles the endpoint call
-   add `path('sample/subsample/', handler_function, name='name_of_sample')`

# How to create and perform migration

In order to find the models to do migration add the path to the model in AppConfig file, when overriding the ready method.

```python
class ApiAppConfig(AppConfig):
    ...

    def ready(self) -> None:
        from apiapp.repositories.movies.models import Movie
        ...
```

To create new migration

```shell
$ python manage.py makemigrations
```

To apply migrations

```shell
$ python manage.py migrate
```

# Main Components

## py_automapper

[py-automapper](https://pypi.org/project/py-automapper/)

> Python auto mapper is useful for multilayer architecture which requires constant mapping between objects from separate layers (data layer, presentation layer, etc).

py-automapper has built-in extension for Pydantic but it does not have one for Django ORM. Blackslope `django_py_automapper_extension` provides this functionality for `django.db` models.

## django-health-check

[django-health-check](https://pypi.org/project/django-health-check/)

The following health checks are bundled with this project:

cache, database, storage, disk and memory utilization (via psutil), AWS S3 storage, Celery task queue, Celery ping,RabbitMQ, Migrations

## pytest-django

With [pytest](https://docs.pytest.org/) you can create and run tests for different units of an application. [pytest-django] (https://pytest-django.readthedocs.io/) is a plugin for pytest with some tools for testing Django application.

Group the test in classes. The class name should start with `Test` and the test methods in that class should start with `test_`. The other classes and methods would be skipped.

## pytest-cov

To get coverage for the apiapp project in the

```shell
$ poetry run pytest --cov
```

## Custom Components

### strong_type decorator

This decorator will automatically inject a strongly typed model into your django controller endpoint. Note that the parentheses are required.

```python
@strong_type()
def my_endpoint(self, request, model: MyModelClass)
    ...
```

By default, the decorator looks for the request in the second position. It must search by position because django passes it as an arg, not a kwarg. Also by default, the decorator will look for a kwarg named model with a type hint and attempt to convert request.data into that type. If you need to specify values other than those defaults, you can do so:

```python
@strong_type(request_position=2, argument_name="model_class")
def my_endpoint(self, something_else, request, model_class: MyModelClass)
    ...
```

Note that request_position is base 0.

## logging

Django contains a logging mechanism that extends the Python???s builtin logging module. Configurations of the logging is defined in `blackslope.settings.py`. The `LOGGING` value will be used to congigure the logging. The default behavior is to log to a file and console. Check the [Django Document](https://docs.djangoproject.com/en/4.0/topics/logging/) for details on logging configurations.
