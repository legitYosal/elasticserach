""" Model Layer """
from elasticsearch import Elasticsearch as _ElkClient
from .utils import config

class BaseElastic:

    def __init__(self, ):
        self.client = _ElkClient(
            hosts=config.ELIK_HOSTS,
            port=config.ELK_PORT,
        )
        self.client.index
    
    def delete(self, index: str, id: str) -> dict:
        return self.client.delete(index=index, id=id)

    def store(self, index: str, body: dict) -> dict:
        result = self.client.index(
            index=index,
            body=body
        )
        return self.client.get(
            index=index, id=result['_id']
        )

class NoteViewElastic(BaseElastic):

    def get_views(self, index: str) -> int:
        return self.client.cat.count(
            index=index, 
        )

class NoteElastic(BaseElastic):

    def get(self, index: str, 
            text_query: str = None,
            title_query: str = None, ) -> dict:

        empty_query = True
        query_dict = {'query':{}}

        if title_query:
            empty_query = False
            query_type = 'match' if len(title_query.split(' ')) > 1 else 'fuzzy'
            query_dict['query'][query_type] = {}
            query_dict['query'][query_type]['title'] = title_query
            print(query_dict)

        if text_query:
            empty_query = False
            query_dict['query']['match'] = {}
            query_dict['query']['match']['text'] = text_query 

        return self.client.search(
            index=index,
            body=query_dict if not empty_query else {}
        )

    