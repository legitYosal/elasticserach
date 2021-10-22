""" Controller Layer """
from .elastic import ElasticSearch
from .utils.wrappers import get_elk_client

class NoteBook:
    """
        The layer that is responsible managing requests from client and
        interacting with storage layer... it is controller
    """

    NOTEBOOK_INDEX = 'notebooks'

    @classmethod
    @get_elk_client
    def get(cls, elk_client: ElasticSearch) -> dict:
        return elk_client.get(index=cls.NOTEBOOK_INDEX)

    @classmethod
    @get_elk_client
    def create(cls, title: str, body: str, elk_client: ElasticSearch) -> dict:
        result = elk_client.store(index=cls.NOTEBOOK_INDEX, body={
            'title':title,
            'body':body
        })
        return result
