from functools import wraps

def return_response(fn):
    __doc__ = '''Decorator for generally getting a Response.text object'''
    @wraps(fn)
    def wrapped(*args, **kwargs):
        response = fn(*args, **kwargs)
        if not response.status_code:
            return response.status_code
        return response.text
    return wrapped
