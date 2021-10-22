from elasticsearch import Elasticsearch as _ElkClient
from . import config

class ElasticSearch:

    def __init__(self, ):
        self.client = _ElkClient(
            hosts=config.ELIK_HOSTS,
            port=config.ELK_PORT,
        )


    