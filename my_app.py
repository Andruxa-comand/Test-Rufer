from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()

        layout = QVBoxLayout()
        layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = secondWin()
    

app = QApplication([])
main_win = MainWin()
app.exec_()



