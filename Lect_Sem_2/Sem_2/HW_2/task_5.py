'''
    Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
    При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/select_form/', methods=['GET', 'POST'])
def select_form():
    if request.method == 'POST': # Если POST, то пользователь что то отправил с нашей формы
        action = request.form.get('Operation')
        f_num = int(request.form.get('first_number'))
        s_num = int(request.form.get('second_number'))
        match action:
            case 'Addition':
                return str(f_num + s_num)
            case 'Subtraction':
                return str(f_num - s_num)
            case 'Multiplication':
                return str(f_num * s_num)
            case 'Division':
                if s_num != 0:
                    return str(f_num / s_num)
                else:
                    return f'На ноль делить нельзя'
    return render_template('t5_form.html')

if __name__ == '__main__':
    app.run() 