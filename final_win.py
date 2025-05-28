from instr import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout

class finalWin(QWidget):
    def __init__(self, exp): # ДОБАВИТЬ exp в init (слайд 17 из Подсчет результатов)
        super().__init__()
        # ЗДЕСЬ ВСТАВИТЬ новую строку из слайда
        self.exp = exp
        self.setAppear()
        self.initUI()
        self.show()

    # ДОБАВЛЕНА функция из Подсчет результатов. Слайды 18 и 23
    # Нудно чуть дописать и разобраться
    def results(self):
        # Дополнительное условие
        if int(self.exp.age) < 7:
            self.index = 0

        # То что дано в презентации
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
        
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.4 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.4 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.4 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 17.9 and self.index >= 14:
                return txt_res2
            elif self.index < 13.9 and self.index >= 9:
                return txt_res3
            elif self.index < 8.9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.4 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.4 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.4 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 20.9 and self.index >= 17:
                return txt_res2
            elif self.index < 16.9 and self.index >= 12:
                return txt_res3
            elif self.index < 11.9 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        # Остальные условия также но по таблице из слайда 19 Подсчет результатов
        # Изменяем лишьь числа с возрастом и коэффициенты индекса
        # Еще 5 таких же условий


    def setAppear(self):
        self.setWindowTitle(txt_finalwin) #ИЗМЕНЕНА переменную
        self.resize(win_width, win_height) # ИЗМЕНЕНА  переменные 
        self.move(win_x, win_y) # ИЗМЕНЕНА переменные 

    def initUI(self): 
        # ДоБАВЛЕНО отображение результата
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index = QLabel(txt_index + str(self.index))

        self.lay = QVBoxLayout()
        # ДОБАВЛЕНО выравнивание
        self.lay.addWidget(self.workh_text, alignment =Qt.AlignCenter)
        self.lay.addWidget(self.index, alignment =Qt.AlignCenter)

        # ДОБАВЛЕНО отображение линий
        self.setLayout(self.lay)
# УБРАТЬ здесь уже нет кнопки
    # def nextClick(self):
    #     self.hide()