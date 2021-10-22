from typing import Callable
from ..elastic import ElasticSearch

def get_elk_client(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        if not kwargs.get('elk_client', None):
            kwargs['elk_client'] = ElasticSearch()
        return func(*args, **kwargs)

    return wrapper