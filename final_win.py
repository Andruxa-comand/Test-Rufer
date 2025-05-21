from instr import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from final_win import*

class finalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setAppear()
        self.initUI()
        self.show()

    def setAppear(self):
        self.setWindowTitle(txt_test2)
        self.resize(win_x, win_y)
        self.move(win_width, win_height)
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index = QLabel(txt_index)

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.workh_text, Qt.AlignCenter)
        self.lay.addWidget(self.index, Qt.AlignCenter)