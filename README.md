# py-blackslope

Python implementation of BlackSlope

## Other BlackSlope Implementations

-   [BlackSlope.NET](https://github.com/SlalomBuild/blackslope.net) is the .NET implementation of the BlackSlope.

# How to run

## Install dependencies

```shell
$ poetry install
```

## Initialize the environment

For local environment a ".env" file should be created under the blackslope folder. This file contains the secretes for local use. For CI/CD pipeline refer to the user guide for them to create environment variables

```local.env
# Do not check it the .env files which contain secrets
SECRET_KEY=<some_random_secret>
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

# How to add API Endpoint

Py-BlackSlope uses the View Class approach for API endpoints
Create the folder under the operations. In the views file add the class which serve as controllers. Each method in a controller will handle a HTTP method.

Add the Paths to the API in:
the urls.py under the apiapp folder

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

py-automapper has extensions for Pydantic!?

## django-health-check

[django-health-check](https://pypi.org/project/django-health-check/)

The following health checks are bundled with this project:

cache, database, storage, disk and memory utilization (via psutil), AWS S3 storage, Celery task queue, Celery ping,RabbitMQ, Migrations
