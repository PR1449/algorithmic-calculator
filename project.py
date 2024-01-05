import sys
import sqlite3
from math import factorial, sqrt, sin, cos, tan, radians, asin, acos, atan, pi

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('maincalc.ui', self)

        self.pushcalc.clicked.connect(self.open_calc_form)
        self.pushsistem.clicked.connect(self.open_number_system_form)
        self.pushedin.clicked.connect(self.open_uni_form)
        self.pushtrigonom.clicked.connect(self.open_trigonometry_form)
        self.pushyrafnenia.clicked.connect(self.open_equations_form)
        self.pushrevsug.clicked.connect(self.open_reviews_suggestion_form)

        self.label_2.setPixmap(QPixmap('pi.png'))
        self.label_3.setPixmap(QPixmap('sqrt.png'))
        self.label_4.setPixmap(QPixmap('e.png'))
        self.label_5.setPixmap(QPixmap('eq.png'))
        self.label_6.setPixmap(QPixmap('fi.png'))
        self.label_7.setPixmap(QPixmap('lambda.png'))
        self.label_8.setPixmap(QPixmap('tau.png'))
        self.label_9.setPixmap(QPixmap('sign1.png'))
        self.label_10.setPixmap(QPixmap('factorial.png'))
        self.label_11.setPixmap(QPixmap('betta.png'))
        self.label_12.setPixmap(QPixmap('theta.png'))
        self.label_13.setPixmap(QPixmap('div.png'))

    def open_calc_form(self):
        self.calc_form = Calculator()
        self.calc_form.show()

    def open_number_system_form(self):
        self.number_system_form = NumberSystem()
        self.number_system_form.show()

    def open_uni_form(self):
        self.uni_form = UnitsOfMeasurement()
        self.uni_form.show()

    def open_trigonometry_form(self):
        self.trigonometry_form = Trigonometry()
        self.trigonometry_form.show()

    def open_equations_form(self):
        self.equations_form = Equations()
        self.equations_form.show()

    def open_reviews_suggestion_form(self):
        self.reviews_suggestion_form = ReviewsSuggestions()
        self.reviews_suggestion_form.show()


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        uic.loadUi('calc1.ui', self)

        for btn in self.buttonGroup_digits.buttons():
            btn.clicked.connect(self.digits)
        self.btn_dot.clicked.connect(self.dot)

        for btn in self.buttonGroup_binary.buttons():
            btn.clicked.connect(self.binary)
        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_fact.clicked.connect(self.unary)
        self.btn_sqrt.clicked.connect(self.unary)
        self.btn_pow.clicked.connect(self.binary)
        self.data = '0'
        self.exp = '0'

    def digits(self):
        if self.data == '0':
            self.data = self.sender().text()
        else:
            self.data += self.sender().text()

        if self.exp == '0':
            self.exp = self.sender().text()
        else:
            self.exp += self.sender().text()
        self.table.display(self.data)

    def dot(self):
        if '.' in self.data:
            return
        else:
            self.data += self.sender().text()
            self.exp += self.sender().text()
            self.table.display(self.data)

    def binary(self):
        if self.exp[-1] in '-+/^*':
            self.exp = self.exp[:-1] + self.sender().text()
        else:
            self.data = '0'
            try:
                result = str(eval(self.exp.replace('^', '**')))
                self.table.display(result)
                self.exp = result + self.sender().text()
            except:
                self.table.display('Error')
                self.exp = '0'

    def result(self):
        if self.exp[-1] in '-+/^*':
            self.exp = self.exp[:-1]
        self.data = '0'
        try:
            self.exp = str(eval(self.exp.replace('^', '**')))
            self.table.display(self.exp)
        except:
            self.table.display('Error')
            self.exp = '0'

    def clear(self):
        self.data = '0'
        self.exp = '0'
        self.table.display(self.data)

    def unary(self):
        self.data = '0'
        if self.exp[-1] in '-+/^*':
            self.exp = self.exp[:-1]
        try:
            result = eval(self.exp.replace('^', '**'))
            if self.sender().text() == '!':
                self.exp = str(factorial(result))
            else:
                self.exp = f'{sqrt(result):.3}'
            self.table.display(self.exp)
        except:
            self.table.display('Error')
            self.exp = '0'


class NumberSystem(QMainWindow):
    def __init__(self):
        super(NumberSystem, self).__init__()
        uic.loadUi('sistemachislenia.ui', self)

        self.pushButton.clicked.connect(self.des_sec_calc)
        self.pushButton_2.clicked.connect(self.des_eigh_calc)
        self.pushButton_3.clicked.connect(self.des_sixteen_calc)

    def des_sec_calc(self):
        try:
            n, lis = 0, []
            number = int(self.lineEdit.text())
            if number < 2:
                self.lineEdit_2.setText('Перевод невозможен')
            else:
                while number >= 2:
                    n = number % 2
                    number //= 2
                    lis.append(n)
                    if number < 2:
                        lis.append(number)
                a = ''.join([str(x) for x in lis[::-1]])
                self.lineEdit_2.setText(a)
        except:
            self.lineEdit_2.setText('Ошибка ввода')

    def des_eigh_calc(self):
        try:
            n, lis = 0, []
            number = int(self.lineEdit.text())
            if number < 8:
                self.lineEdit_2.setText('Перевод невозможен')
            else:
                while number >= 8:
                    n = number % 8
                    number //= 8
                    lis.append(n)
                    if number < 8:
                        lis.append(number)
                self.lineEdit_2.setText(''.join([str(x) for x in lis[::-1]]))
        except:
            self.lineEdit_2.setText('Ошибка ввода')

    def des_sixteen_calc(self):
        try:
            n, lis = 0, []
            number = int(self.lineEdit.text())
            if number < 16:
                self.lineEdit_2.setText('Перевод невозможен')
            else:
                while number >= 16:
                    n = number % 16
                    number //= 16
                    lis.append(n)
                    if number < 16:
                        lis.append(number)
                self.lineEdit_2.setText(''.join([str(x) for x in lis[::-1]]))
        except:
            self.lineEdit_2.setText('Ошибка ввода')


class UnitsOfMeasurement(QWidget):
    def __init__(self):
        super(UnitsOfMeasurement, self).__init__()
        uic.loadUi('units_measurement.ui', self)

        self.pushButton.clicked.connect(self.write_length)
        self.pushButton_2.clicked.connect(self.write_weigth)
        self.pushButton_3.clicked.connect(self.write_square)
        self.pushButton_4.clicked.connect(self.write_volume)
        self.pushButton_5.clicked.connect(self.help)

    def length(self):
        length_dict = {
            'mm': {'cm': 0.1, 'm': 10**-3, 'km': 10**-6, '"': 0.03937, "'": 0.003281, 'yd': 0.001094},
            'cm': {'mm': 10, 'm': 0.01, 'km': 10*8-3, '"': 0.393701, "'": 0.032808, 'yd': 0.010936},
            'm': {'mm': 1000, 'cm': 10, 'km': 1000000, '"': 39.37008, "'": 3.28084, 'yd': 1.093613},
            'km': {'mm': 1000000, 'cm': 100000, 'm': 1000, '"': 39370.08, "'": 3280.84, 'yd': 1093.613}
            '"': {'mm': 25.4, 'cm': 2.54, 'm': 0.0254, 'km': 0.000025, "'": 0.083333, 'yd': 0.027778}, # inch(дюймы)
            "'": {'mm': 304.8, 'cm': 30.48, 'm': 0.3048, 'km': 0.000305, '"': 12, 'yd': 0.333333}, # foot
            'yd': {'mm':914.4 , 'cm': 91.44, 'm': 0.000914, 'km': 0.000914, '"': 36, "'": 3}
        }
        try:
            start = self.lineEdit.text().split()[0]
            val = self.lineEdit.text().split()[1]
            finish = self.lineEdit_2.text()
            if start.isdigit():
                start, val = val, start
            to_m = length_dict[start.lower()][0] * int(val)
            if length_dict[finish][2] == '*':
                answer = to_m * length_dict[finish.lower()][1]
            else:
                answer = to_m / length_dict[finish.lower()][1]
            return answer
        except:
            return 'Error'

    def write_length(self):
        self.lineEdit_3.setText(str(self.length()))

    def weigth(self):
        weigth_dict = {
            'kg': (1000, 0.001, '*'),
            'g': (1, 1, '*'),
            'mg': (0.001, 1000, '*')}
        try:
            start = self.lineEdit_6.text().split()[0]
            val = self.lineEdit_6.text().split()[1]
            finish = self.lineEdit_5.text()
            if start.isdigit():
                start, val = val, start
            to_m = weigth_dict[start.lower()][0] * int(val)
            if weigth_dict[finish][2] == '*':
                answer = to_m * weigth_dict[finish.lower()][1]
            else:
                answer = to_m / weigth_dict[finish.lower()][1]
            return answer
        except:
            return 'Error'

    def write_weigth(self):
        self.lineEdit_4.setText(str(self.weigth()))

    def square(self):
        square_dict = {
            'km': (1000000, 1, '/'),
            'm': (1, 1, '*'),
            'cm': (0.0001, 10000, '*'),
            'mm': (0.00001, 1000000, '*')}

        try:
            start = self.lineEdit_9.text().split()[0]
            val = self.lineEdit_9.text().split()[1]
            finish = self.lineEdit_8.text()
            if start.isdigit():
                start, val = val, start
            to_m = square_dict[start.lower()][0] * int(val)
            if square_dict[finish][2] == '*':
                answer = to_m * square_dict[finish.lower()][1]
            else:
                answer = to_m / square_dict[finish.lower()][1]
            return answer
        except:
            return 'Error'

    def write_square(self):
        self.lineEdit_7.setText(str(self.square()))

    def volume(self):
        volume_d = {
            'm': (1, 1, '*'),
            'cm': (0.000001, 1000000, '*'),
            'mm': (0.000000001, 1000000000, '*')}

        try:
            start = self.lineEdit_12.text().split()[0]
            val = self.lineEdit_12.text().split()[1]
            finish = self.lineEdit_11.text()
            if start.isdigit():
                start, val = val, start
            to_m = volume_d[start.lower()][0] * int(val)
            if volume_d[finish][2] == '*':
                answer = to_m * volume_d[finish.lower()][1]
            else:
                answer = to_m / volume_d[finish.lower()][1]
            return answer
        except:
            return 'Error'

    def write_volume(self):
        self.lineEdit_10.setText(str(self.volume()))

    def help(self):
        with open('UnitsOfMeasurementhelp.txt', encoding='utf-8') as file:
            f = file.read()
            QMessageBox.about(self, 'Справка', f'{f}')


class Equations(QWidget):
    def __init__(self):
        super(Equations, self).__init__()
        uic.loadUi('equations.ui', self)

        self.pushButton.clicked.connect(self.eqa_roots)
        self.pushButton_2.clicked.connect(self.help)

    def solve(self):
        try:
            string = [float(i) for i in str(self.lineEdit.text()).split()]
            sp = list(string)
            res = []
            if len(sp) >= 4 or not bool(sp):
                return None
            if len(sp) == 3 and sp[0] != 0:
                a, b, c = sp[0], sp[1], sp[2]
                if a == b == c == 0:
                    res.append('Любое число')
                    return res
                else:
                    D = b ** 2 - 4 * a * c
                    if D > 0:
                        x1 = (-b + D ** 0.5) / (2 * a)
                        x2 = (-b - D ** 0.5) / (2 * a)
                        res.append(x1)
                        res.append(x2)
                        return res
                    elif D == 0:
                        x = -b / (2 * a)
                        res.append(x)
                        return res
                    else:
                        return 'Корней нет'
            if len(sp) == 3 and sp[0] == 0:
                a, c = sp[0], sp[1]
                if a == c == 0:
                    res.append('Любое число')
                    return res
                else:
                    x = -c / a
                    res.append(x)
                    return res
            if len(sp) == 2 and sp[0] != 0:
                a, b = sp[0], sp[1]
                if a == b == 0:
                    res.append('Любое число')
                    return res
                else:
                    x2 = (-b / a)
                    res.append(x2)
                    return res
            if len(sp) == 2 and sp[0] == 0:
                if sp[0] != sp[1]:
                    res.append('Решений нет')
                    return res
                else:
                    res.append('Любое число')
                    return res
            if len(sp) == 1:
                if sp[0] != 0:
                    res.append(0)
                    return res
                else:
                    res.append('Любое число')
                    return res

        except:
            return 'Ошибка ввода'

    def eqa_roots(self):
        x = self.solve()
        if len(x) == 2:
            self.lineEdit_2.setText(' и '.join([str(i) for i in sorted(x)]))
        elif type(x[0]) != str:
            self.lineEdit_2.setText(*list(map(str, x)))
        else:
            self.lineEdit_2.setText(''.join(x))

    def help(self):
        with open('Equationshelp.txt', encoding='utf-8') as file:
            f = file.read()
            QMessageBox.about(self, 'Справка', f'{f}')


class Trigonometry(QWidget):
    def __init__(self):
        super(Trigonometry, self).__init__()
        uic.loadUi('trigonometry.ui', self)

        self.pushButton_2.clicked.connect(self.sinx)
        self.pushButton.clicked.connect(self.cosx)
        self.pushButton_4.clicked.connect(self.tanx)
        self.pushButton_5.clicked.connect(self.asinx)
        self.pushButton_6.clicked.connect(self.acosx)
        self.pushButton_8.clicked.connect(self.atanx)
        self.pushButton_3.clicked.connect(self.ctgx)
        self.pushButton_7.clicked.connect(self.actgx)
        self.pushButton_9.clicked.connect(self.help)

    def sinx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(sin(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def cosx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(cos(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def tanx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(tan(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def asinx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(asin(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def acosx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(acos(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def atanx(self):
        try:
            x = self.lineEdit.text()
            self.lineEdit_3.setText(str(atan(radians(int(x)))))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def ctgx(self):
        try:
            x = radians(int(self.lineEdit.text()))
            ctg = cos(x) / sin(x)
            self.lineEdit_3.setText(str(ctg))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def actgx(self):
        try:
            x = radians(int(self.lineEdit.text()))
            actg = pi / 2 - atan(x)
            self.lineEdit_3.setText(str(actg))
        except:
            self.lineEdit_3.setText('Ошибка ввода')

    def help(self):
        with open('Trigonometryhelp', encoding='utf-8') as file:
            f = file.read()
            QMessageBox.about(self, 'Справка', f'{f}')


class ReviewsSuggestions(QWidget):
    def __init__(self):
        super(ReviewsSuggestions, self).__init__()
        uic.loadUi('reviews&suggestions.ui', self)

        self.con = sqlite3.connect('db_project')
        self.pushButton.clicked.connect(self.reviews)
        self.pushButton_2.clicked.connect(self.suggestions)

    def reviews(self):
        cur = self.con.cursor()
        valid = QMessageBox.question(self, 'Отзывы',
                                     'Вы хотите оставить отзыв?',
                                     QMessageBox.Yes, QMessageBox.No)
        if valid != QMessageBox.Yes:
            return
        text = self.textEdit.toPlainText()
        cur.execute(f'insert into reviews(review) values("{text}")')
        self.con.commit()
        QMessageBox.about(self, ' ', 'Ваш отзыв успешно сохранён.')
        self.con.close()

    def suggestions(self):
        cur = self.con.cursor()
        valid = QMessageBox.question(self, 'Предложения',
                                     'Оставить предложения по улучшению работы калькулятора?',
                                     QMessageBox.Yes, QMessageBox.No)
        if valid != QMessageBox.Yes:
            return
        text = self.textEdit.toPlainText()
        cur.execute(f'insert into suggestions(suggestion) values("{text}")')
        self.con.commit()
        QMessageBox.about(self, ' ', 'Ваше предложение успешно сохранено.')
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())
