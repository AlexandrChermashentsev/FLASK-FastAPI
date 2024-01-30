'''
    Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
    При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
где будет выведено "Привет, {имя}!".
'''

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key =b'd8d876fa4dbc29b1f2163ed1665c399bc3be0a1c6910a162d0ef65dd4f01932b'

@app.route('/')
def index():
    return 'Hi!'

@app.route('/form_flash/', methods=['GET', 'POST'])
def form_flash():
    if request.method == 'POST':
        name = request.form.get('name')
    # Обработка данных формы
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form_flash'))
    return render_template('t8_flash_form.html')

if __name__ == '__main__':
    app.run()