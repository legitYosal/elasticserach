from threading import get_ident
from datetime import datetime
from app.notes import Note, NoteViews
from app.elastic import NoteViewElastic
from app.postgres import NoteViewsSQL

class BaseAgent:
    """
        agent just views a note and emits the action to
        storage
    """
    def log(self, *args, **kwargs):
        print('INFO: TID:' + str(get_ident()) + ' => ', *args, **kwargs)

    def run(self, ):
        """
            - get all notes
            - for all notes
                - emit viewed
        """
        notes = Note.get()['hits']['hits']

        while True:
            import time
            from random import randint
            time.sleep(0.05)
            for index, note in enumerate(notes):
                if randint(1, 10) * index // 5 > 1:
                    self.emit(note['_id'])

    def emit(self, note_id: str):
        raise NotImplemented

class ElasticAgent(BaseAgent):

    def __init__(self, ):
        self.client = NoteViewElastic()

    def emit(self, note_id: str):
        index_str = NoteViews.get_note_views_index()
        self.log(index_str)
        self.client.store(index=index_str, body={
            'creted_at': str(datetime.now()),
            'note_id': note_id,
        })

class PostgresAgent(BaseAgent):
    def __init__(self, ):
        self.client = self.get_connection()
        self.commits = 0

    def get_connection(self, ):
        return NoteViewsSQL()

    def emit(self, note_id: str):
        self.log(' INSERT FOR ' + note_id)
        self.client.insert(note_id)