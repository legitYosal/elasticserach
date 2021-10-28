""" API Layer """
from fastapi import FastAPI

from src.notebook import NoteBook

app = FastAPI()


@app.get('/note-book/')
def get_notebooks():
    return NoteBook.get()

@app.post('/note-book/')
def get_notebooks(notebook: NoteBook.Body):
    return NoteBook.create(
        title=notebook.title,
        body=notebook.body
    )

if __name__ == '__main__':
    print("""
        Run run_srcirpt.sh and go to http://localhost:8000/docs
    """)