from flask import Flask, render_template, redirect

from login_form import LoginForm

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = {
        "title": "Заголовок"
    }
    return render_template('index.html', **data)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        prof = "Инженерные тренажеры"
    else:
        prof = "Научные симуляторы"
    data = {
        "prof": prof,
        "image": f"/static/img/{prof}.jpg"
    }
    return render_template('training.html', **data)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    list_prof_array = ["Инженер", "Строитель", "Врач", "Программист", "Пилот"]
    data = {
        "type_list": type_list,
        "list_prof": list_prof_array
    }
    return render_template('list_prof.html', **data)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = [
        {
            "key": "Фамилия",
            "value": "Анкета"
        },
        {
            "key": "Имя",
            "value": "Иван"
        },
        {
            "key": "Образование",
            "value": "среднее"
        },
        {
            "key": "Профессия",
            "value": "пилот"
        },
        {
            "key": "Пол",
            "value": "male"
        },
        {
            "key": "Мотивация",
            "value": "хочу побывать на Марсе"
        },
        {
            "key": "Готовы остаться на Марсе",
            "value": True
        }
    ]
    return render_template('answer.html', data=data, title="Анкета")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


app.config['SECRET_KEY'] = 'key'

if __name__ == '__main__':
    app.run()
