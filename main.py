from src import notebook
from src.notebook import NoteBook
from src.elastic import ElasticSearch

if __name__ == '__main__':
    print(NoteBook.create(title='test', body='my body'))
    print(NoteBook.get())