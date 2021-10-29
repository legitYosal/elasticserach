from threading import get_ident
from datetime import datetime
from app.notes import Note, NoteViews
from app.elastic import NoteViewElastic

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
            time.sleep(0.05)
            for note in notes:
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
            'creted_at': str(datetime.now())
        })