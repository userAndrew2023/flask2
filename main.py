from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = {
        "title": "Заголовок"
    }
    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run()
