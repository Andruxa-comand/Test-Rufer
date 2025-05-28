from instr import*
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class secondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setAppear()
        self.initUI()
        self.connets()
        self.show()
    def setAppear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_width, win_height)
    def initUI(self): 
        # Данная функция изменена, можно просто скопировать и понять, что изменено)
        self.hLay = QHBoxLayout()
        self.rLay = QVBoxLayout()
        self.lLay = QVBoxLayout()

        self.name = QLabel(txt_name)
        self.enterName = QLineEdit()
        self.age = QLabel(txt_age)
        self.enterAge = QLineEdit()
        self.test1 = QLabel(txt_test1)
        self.button1 = QPushButton(txt_starttest1) # ДОБАВИТЬ переменную
        self.enterTest1 = QLineEdit()
        self.test2 = QLabel(txt_test2)
        self.button2 = QPushButton(txt_starttest2) # ДОБАВИТЬ переменные 
        self.enterTest2 = QLineEdit()
        self.test3 = QLabel(txt_test3)
        self.button3 = QPushButton(txt_starttest3) # ДОБАВИТЬ переменные 
        self.enterTest3 = QLineEdit() # ДОБАВИТЬ переменные и ИЗМЕНЕНО название
        # self.enterTest32 = QLineEdit() # УБРАТЬ не нужна вторая
        self.text_timer = QLabel(txt_timer) # ДОБАВИТЬ переменные и ИЗМЕНЕНО название 
        
        self.buttonNext = QPushButton(txt_sendresults)
        # ДОБАВИТ просто чтобы красиво было. Добавляется текстовая подсказка
        self.enterName.setPlaceholderText(txt_hintname)
        self.enterAge.setPlaceholderText(txt_hintage)
        self.enterTest1.setPlaceholderText(txt_hinttest1)
        self.enterTest2.setPlaceholderText(txt_hinttest2)
        self.enterTest3.setPlaceholderText(txt_hinttest3)
        # ИЗМЕНЕН правилный порядок и ДОБАВЛЕНО выравнивание по левому краю
        self.rLay.addWidget(self.name, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterName, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.age, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterAge, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterTest1, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.button3, alignment= Qt.AlignLeft) #это добавлено
        self.rLay.addWidget(self.enterTest2, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterTest3, alignment= Qt.AlignLeft) # изменено на правилное название
        self.rLay.addWidget(self.buttonNext, alignment= Qt.AlignCenter)  #это добавлено
        self.lLay.addWidget(self.text_timer, alignment= Qt.AlignCenter)
        
        self.hLay.addLayout(self.rLay)
        self.hLay.addLayout(self.lLay)
        self.setLayout(self.hLay)  
    
    def timer_test(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Timer", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time 
        time = QTime(0, 0, 31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Timer", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0")
        self.text_timer.setFont(QFont("Timer", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connets(self):
        self.buttonNext.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.enterAge.text()), self.enterTest1.text(), self.enterTest2.text(), self.enterTest3.text())
        # ДОБАВЛЕНА оправка в окно
        self.tw = finalWin(self.exp)