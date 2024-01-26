from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'


@app.route('/about/')
def about():
    context = {'title': "О нас"}
    return render_template('about.html', **context)

@app.route('/contacts/')
def contacts():
    context = {'title': "Контакты"}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run()