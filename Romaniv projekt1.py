import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

app=QApplication([])
main=QWidget()

main.setWindowTitle("Калькулятор")
main.resize(800,500)
layout1=QVBoxLayout()
layout2=QFormLayout()
q1=QLabel("Введіть число 1:")
j1=QLineEdit()
q2=QLabel("Введіть число 2:")
j2=QLineEdit()
q3=QLabel("Введіть дію:")
j3=QLineEdit()
button1=QPushButton("Calculate")
line1=QVBoxLayout()
line2=QVBoxLayout()
line3=QVBoxLayout()
line4=QVBoxLayout()
line1.addWidget(q1,alignment=Qt.AlignCenter)
line1.addWidget(j1,alignment=Qt.AlignCenter)
line2.addWidget(q2,alignment=Qt.AlignCenter)
line2.addWidget(j2,alignment=Qt.AlignCenter)
line3.addWidget(q3,alignment=Qt.AlignCenter)
line3.addWidget(j3,alignment=Qt.AlignCenter)
line4.addWidget(button1,alignment=Qt.AlignCenter)

superl=QVBoxLayout()
superl.addLayout(line1)
superl.addLayout(line2)
superl.addLayout(line3)
superl.addLayout(line4)

main.setLayout(superl)

#button1.clicked.connect(win)





main.show()
app.exec_()