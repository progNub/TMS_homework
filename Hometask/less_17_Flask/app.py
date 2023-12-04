from flask import Flask, render_template, request
from sqlalchemy.exc import IntegrityError

from models import add_note, get_uuid, get_note, create_tables
from exeptions import EmptyError

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main_page.html')


@app.route('/', methods=['POST'])
def add_note_view():
    data = request.form
    try:
        add_note(data['title'], data['content'])
    except EmptyError:
        error = 'Поля title и content не могут быть пустыми'
        return render_template('main_page.html', error=error, data=data)
    except IntegrityError:
        error = 'Поле title должно быть уникальным'
        return render_template('main_page.html', error=error, data=data)
    uuid = get_uuid(data['title'])
    return render_template('uuid_page.html', uuid=uuid)


@app.route('/<uuid>', methods=['GET'])
def get_note_view(uuid: str):
    note = get_note(uuid)
    if not note:
        return render_template('note_page.html', error='нет записи с таким uuid')
    else:
        return render_template('note_page.html', note=note.to_dict())


if __name__ == '__main__':
    create_tables()
    app.run()
