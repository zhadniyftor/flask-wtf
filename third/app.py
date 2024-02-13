from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<title>')
def index(title: str = ''):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str):
    return render_template('training.html', profession=prof)


@app.route('/list_prof/<param>')
def jobs_list(param=None):
    error = param not in ['ol', 'ul']
    jobs_list = ['Витя', "Петя", "Олег", "Конь в пальто"]
    return render_template(
        'jobs_list.html', error=error, list=jobs_list, param=param
    )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
