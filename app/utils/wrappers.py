from typing import Callable
from ..elastic import NoteElastic

def get_note_elk_client(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        if not kwargs.get('elk_client', None):
            kwargs['elk_client'] = NoteElastic()
        return func(*args, **kwargs)

    return wrapper