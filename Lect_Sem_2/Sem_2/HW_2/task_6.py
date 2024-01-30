'''
    Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
    При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
'''

from flask import Flask, render_template, request
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/')
def base():
    return render_template('base.html')


@app.post('/user_form/')
def user_post():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    if age < 0 or age > 120:
        return render_template('404.html')
    else: 
        return f'Hello {name}, {age} years old!'

@app.get('/user_form/')
def user_get():
    return render_template('t6_form.html')


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
               'title': 'Некорректно введен возраст',
               'url': request.base_url,}
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run() 