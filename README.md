from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


card_width, card_height = 600, 500 #початкові розміри вікна "картка"
app=QApplication([])
win_card = QWidget()

win_card.resize(card_width, card_height)

win_card.move(300, 300)

win_card.setWindowTitle('Memory Card')

btn_Sleep = QPushButton("Відпочити")
box_Minutes=QSpinBox()
box_Minutes.setValue(30)
btn_menu=QPushButton("Меню")
btn_menu=QPushButton("Відповісти")
sp_rest= QSpinBox()
RadioGroupBox=QGroupBox("Варіанти відповідей")
RadioGroup=QButtonGroup()
rbtn_ans1=QRadioButton("1")
rbtn_ans2=QRadioButton("2")
rbtn_ans3=QRadioButton("3")
rbtn_ans4=QRadioButton("4")
RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

layout_ans1 = QHBoxLayout()   

layout_ans2 = QVBoxLayout()

layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_ans1) #Дві відповіді в перший стовпець

layout_ans2.addWidget(rbtn_ans2)

layout_ans3.addWidget(rbtn_ans3) #Дві відповіді у другий стовпець

layout_ans3.addWidget(rbtn_ans4)

AnsGroupBox=QGroupBox("Результат теста")
lb_Result=QLabel("")
lb_Correct=QLabel("")

#Тепер перемикачі прив'язані до однієї горизонтальної направляючої лінії

layout_ans1.addLayout(layout_ans2)

layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1)


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter , stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
# win_card.setLayout(RadioGroupBox)
# win_card.show()
# app.exec_()
