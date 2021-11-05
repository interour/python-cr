import typing

# Annotate the HTTP endpoint our function will be serving. To be used by our future
# HTTP framework.
#
# Path components may contain "{keyword}" substring and such substrings will be then
# passed to the decorated function by the framework engine.
def endpoint(path: str) -> typing.Callable[..., typing.Any]:
    def annotating(fn: typing.Callable[..., typing.Any]) -> typing.Callable[..., typing.Any]:
        fn.http_endpoint_path = path
        return fn

    return annotating
