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


def error404():
    return "УПС. Эта страница не найдена"


if __name__ == '__main__':
    app.run()
