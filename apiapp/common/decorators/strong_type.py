from inspect import signature

from pydantic import parse_obj_as


def strong_type(request_position: int = 1, argument_name: str = "model"):
    def decorator_wrapper(fn):
        def wrapper(*args, **kwargs):
            print(args)
            sig = signature(fn)
            t: type = sig.parameters[argument_name].annotation
            data = parse_obj_as(t, args[request_position].data)
            kwargs[argument_name] = data

            return fn(*args, **kwargs)

        return wrapper

    return decorator_wrapper
