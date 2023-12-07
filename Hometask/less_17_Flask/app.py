from flask import Flask, render_template, request, redirect
from sqlalchemy.exc import IntegrityError

from models import create_tables
from crud import add_note, get_uuid, get_note, get_all_notes
from exeptions import EmptyError

app = Flask(
    __name__,
    template_folder="templates",
    # Путь, по которому можно получить файлы их папки `static_folder`.
)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main_page.html',  notes=get_all_notes())


@app.route('/', methods=['POST'])
def add_note_view():
    data = request.form
    try:
        add_note(data['title'], data['content'])
    except EmptyError:
        error = 'Поля title и content не могут быть пустыми'
        return render_template('main_page.html', error=error, data=data, notes=get_all_notes())
    except IntegrityError:
        error = 'Поле title должно быть уникальным'
        return render_template('main_page.html', error=error, data=data, notes=get_all_notes())
    return redirect('/')


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
