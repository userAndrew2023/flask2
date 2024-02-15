from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
