'''
    Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
    При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')


@app.post('/number_form/')
def number_post():
    number = request.form.get('number')
    if number.isdigit(): # Целое положительное число
        return f'(1) Квадрат числа {number} = {int(number) ** 2}'
    elif number[0] == '-' and number[1:].isdigit(): # Целое отрицательное число
        return f'(2)Квадрат числа {number} = {int(number) ** 2}'
    else:
        for i in number:
            if i.isalpha():
                return f'Error: {number}!'
            else: return f'(3) Квадрат числа {number} = {float(number) ** 2}'
            
            
@app.get('/number_form/')
def number_get():
    return render_template('t7_form.html')


if __name__ == '__main__':
    app.run() 