""" Controller Layer """
from datetime import datetime
from pydantic import BaseModel
from .elastic import NoteElastic, NoteViewElastic
from .utils.wrappers import get_note_elk_client

class NoteViews:
    NOTEVIEWS_INDEX_PREFIX = 'note_views_index'

    @classmethod
    def get_note_views_index(cls,) -> str:
        # e.g. 'note_views_index_2021-10-28_19_59'
        now = datetime.now()
        time_str = str(now.date()) + '_' + str(now.hour) + '_' + str(now.minute)
        return f'{cls.NOTEVIEWS_INDEX_PREFIX}_{time_str}'

    @classmethod
    def get_noteviews(cls, ) -> dict:
        client = NoteViewElastic()
        notes = [{
            'id': note['_id'],
            'title': note['_source']['title'],
            'text': note['_source']['text'],
            'views': client.get_views('note_views_index_2021-10-28_22_33'),
        } for note in Note.get()['hits']['hits']]
        return notes

class Note:
    """
        The layer that is responsible managing requests from client and
        interacting with storage layer... it is controller
    """

    class Body(BaseModel):
        title: str
        text: str

    NOTE_INDEX = 'notes_index'

    @classmethod
    @get_note_elk_client
    def get(cls, elk_client: NoteElastic, title_query: str = None,
                text_query: str = None) -> dict:

        return elk_client.get(
            index=cls.NOTE_INDEX,
            title_query=title_query,
            text_query=text_query
        )

    @classmethod
    @get_note_elk_client
    def create(cls, title: str, text: str, elk_client: NoteElastic) -> dict:
        result = elk_client.store(index=cls.NOTE_INDEX, body={
            'title': title,
            'text': text
        })
        return result

    @classmethod
    @get_note_elk_client
    def delete(cls, id: str, elk_client: NoteElastic) -> dict:
        result = elk_client.delete(index=cls.NOTE_INDEX, id=id)
        return result
