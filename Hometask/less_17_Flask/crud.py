from sqlalchemy import select, Select

from exeptions import EmptyError
from models import session, Note


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


def get_all_notes():
    with session() as sess:
        query = select(Note)
        notes = sess.execute(query).scalars().all()
    return notes[::-1]

