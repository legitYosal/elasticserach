""" Model Layer """
from elasticsearch import Elasticsearch as _ElkClient
from .utils import config

class ElasticSearch:

    def __init__(self, ):
        self.client = _ElkClient(
            hosts=config.ELIK_HOSTS,
            port=config.ELK_PORT,
        )
        self.client.index

    def store(self, index: str, body: dict) -> dict:
        result = self.client.index(
            index=index,
            body=body
        )
        return result

    def get(self, index: str) -> dict:
        return self.client.search(index=index)

    