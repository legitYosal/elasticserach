from typing import Tuple
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (
    Table, Column, Integer, String, func
)
from app.utils import config

class NoteViewsSQL:
    TABLE_NAME = 'noteviews'
    def __init__(self, ):
        engine = sqlalchemy.create_engine(config.POSTGRESURI)
        self.Session = scoped_session(sessionmaker(bind=engine))
        self.connection = engine.connect()
        metadata = sqlalchemy.MetaData()
        self.NoteViewsTable = Table(
            self.TABLE_NAME, metadata,
            Column('id', Integer, primary_key = True, autoincrement=True), 
            Column('note_id', String(128))
        )
        metadata.create_all(engine)
    
    def insert(self, note_id: str) -> None:
        ins = self.NoteViewsTable.insert().values(note_id=note_id)
        result = self.connection.execute(ins)

    def get_noteviews_count(self, note_id: str) -> Tuple[int, int]:
        import time

        session = self.Session()
        now = time.time()
        res = session.execute(
            f'select count(*) from {self.TABLE_NAME} where {self.TABLE_NAME}.note_id = :note_id', 
            {'note_id':note_id}
        ).fetchall()
        endt = (time.time() - now) * 100
        self.Session.remove()
        return res[0][0], endt

