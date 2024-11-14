import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout) # application handler, empty GUI widget
from PyQt5.QtGui import QIcon

class Calculator(QWidget): # QWidget 클래스를 상속받아서 클래스를 정의

    def __init__(self):
        super().__init__() # 부모 클래스 QWidget을 초기화
        self.initUI() # 나머지 초기화는 initUI 함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)
        # vbox.addWidget(self.btn1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator') # 윈도우에 표시되는 타이틀
        self.setWindowIcon(QIcon('calculator.png'))
        self.resize(256,256) # 윈도우 사이즈
        self.show() # 윈도우 화면이 표시되도록 호출

    def activateMessage(self):
        # QMessageBox.information(self, 'information', 'Button Clicked!')
        self.te1.appendPlainText('Button clicked!')
    
    def clearMessage(self):
        self.te1.clear()

if __name__=='__main__': # pyqt는 애플리케이션 당 1개의 QApplication이 필요
    app = QApplication(sys.argv) # QApplication 인스턴스 생성
    view = Calculator() # Calculator 윈도우 인스턴스 생성
    sys.exit(app.exec_()) # application이 이벤트 처리를 하도록 루프 구동