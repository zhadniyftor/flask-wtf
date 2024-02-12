from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<title>')
def index(title: str = ''):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str):
    return render_template('training.html', profession=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
