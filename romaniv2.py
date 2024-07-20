from PyQt5 import QtCore, QtGui, QtWidgets
import requests  # Make sure to install the requests library

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 260, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 210, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 290, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 120, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit)

        self.pushButton.clicked.connect(self.translate_text)  # Connect button click to the function
        self.comboBox.currentIndexChanged.connect(self.translate_text)  # Connect comboBox change to the function
        self.comboBox_2.currentIndexChanged.connect(self.clear_text)  # Connect comboBox_2 change to clear text fields

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "перекласти"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Англійська"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Китайська"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Іспанська"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Французька"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Арабська"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Українська"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Португальська"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Індонезійська"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Японська"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Німецька"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Англійська"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Китайська"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Іспанська"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Французька"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Арабська"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Українська"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Португальська"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Індонезійська"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Японська"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Німецька"))

    def translate_text(self):
        source_text = self.lineEdit.text()
        source_lang = self.comboBox_2.currentText()
        target_lang = self.comboBox.currentText()

        # Mapping language names to language codes (this can be expanded as needed)
        lang_code_map = {
            "Англійська": "en",
            "Китайська": "zh",
            "Іспанська": "es",
            "Французька": "fr",
            "Арабська": "ar",
            "Українська": "uk",
            "Португальська": "pt",
            "Індонезійська": "id",
            "Японська": "ja",
            "Німецька": "de"
        }

        source_lang_code = lang_code_map.get(source_lang, "en")
        target_lang_code = lang_code_map.get(target_lang, "en")

        translated_text = self.perform_translation(source_text, source_lang_code, target_lang_code)
        self.lineEdit_2.setText(translated_text)

    def clear_text(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def perform_translation(self, text, source_lang, target_lang):
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": source_lang,
            "tl": target_lang,
            "dt": "t",
            "q": text,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
            translated_text = result[0][0][0]
            return translated_text
        else:
            return "Error translating text"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
