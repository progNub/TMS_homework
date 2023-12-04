from sqlalchemy import create_engine, Column, String, Text, DateTime, select, Select
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from datetime import datetime
import uuid
from exeptions import EmptyError

dns = 'sqlite:///my.db'

engine = create_engine(dns, echo=True)
session = sessionmaker(bind=engine, autoflush=False)


def create_tables(eng=engine):
    Base.metadata.create_all(eng)


def drop_tables(eng=engine):
    Base.metadata.drop_all(eng)


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = 'notes'
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(100), unique=True, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем дату для JSON
        }


def add_note(title, content, session=session):
    if title or content:
        with session() as sess:
            note = Note(title=title, content=content)
            sess.add(note)
            sess.commit()
    else:
        raise EmptyError('title and content can`t be empty')


def get_note(uuid_):
    with session() as sess:
        note = Select(Note).where(Note.uuid == uuid_)
        res_note = sess.execute(note).scalar()

    return res_note


def get_uuid(title):
    with session() as sess:
        note = select(Note.uuid).filter_by(title=title)
        res_uuid = sess.execute(note).scalar()
    return res_uuid


if __name__ == '__main__':
    drop_tables()
    create_tables()
