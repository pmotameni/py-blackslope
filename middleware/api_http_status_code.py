import enum

from middleware.description_enum_meta import DescriptionEnumMeta


class ApiHttpStatusCode(enum.Enum, metaclass=DescriptionEnumMeta):
    OK = 200, "OK."
    Created = 201, "Created."
    BadRequest = 400, "Bad Request."
    Unauthorized = 401, "Unauthorized."
    InternalServerError = 500, "Internal Server Error."
