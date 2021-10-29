""" API Layer """
from fastapi import FastAPI

from .notes import Note, NoteViews

app = FastAPI()


@app.get('/notes/')
def get_notes(title_query: str = None, text_query: str = None):
    return Note.get(title_query=title_query, text_query=text_query)

@app.delete('/notes/id/')
def get_notes(id: str):
    return Note.delete(id=id)

@app.post('/notes/')
def create_note(note: Note.Body):
    return Note.create(
        title=note.title,
        text=note.text
    )

@app.get('/note/views/elk/')
def get_note_views():
    return NoteViews.get_noteviews()

if __name__ == '__main__':
    print("""
        Run run_srcirpt.sh and go to http://localhost:8000/docs
    """)