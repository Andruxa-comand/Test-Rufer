from instr import*
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*

class secondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setAppear()
        self.initUI()
        self.connets()
        self.next_click()
        self.show()
    def setAppear(self):
        self.setWindowTitle(txt_test2)
        self.resize(win_x, win_y)
        self.move(win_width, win_height)
    def initUI(self):
        self.hLay = QHBoxLayout()
        self.rLay = QVBoxLayout()
        self.lLay = QVBoxLayout()
   
        self.name = QLabel(txt_name)
        self.enterName = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.enterAge = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.button1 = QPushButton()
        self.enterTest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.button2 = QPushButton()
        self.enterTest2 = QLineEdit(txt_hinttest2)
        self.test3 = QLabel(txt_test3)
        self.button3 = QPushButton()
        self.enterTest31 = QLineEdit()
        self.enterTest32 = QLineEdit()
        self.timer = QLabel()
        
        self.buttonNext = QPushButton()
    
        self.rLay.addWidget(self.enterTest32, alignment= Qt.AlignLeft)
        self.rLay.addWidget(self.enterTest31, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.test3, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.enterTest2, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.button2, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.test2, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.enterTest1, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.button1, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.test1, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.enterAge, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.age, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.enterName, alignment= Qt.AlignCenter)
        self.rLay.addWidget(self.name, alignment= Qt.AlignCenter)
        self.lLay.addWidget(self.timer, alignment= Qt.AlignCenter)
        
        self.hLay.addLayout(self.rLay)
        self.hLay.addLayout(self.lLay)

        self.setLayout(self.hLay)  
    
    def timer_test(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Timer", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time 
        time = QTime(0, 0, 30)
        time = time.addSecs(-1)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Timer", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timet.stop()

    def timer_final(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer3Event)

    def timer3Events(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0")

    def connets(self):
        self.buttonNext.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    
    def next_click(self):
        self.hide()
        self.tw = finalWin()


app = QApplication([])
scndwn = secondWin()
app.exec_()