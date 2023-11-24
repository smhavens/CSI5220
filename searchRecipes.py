from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUiSearch(self, MainWindow):
        MainWindow.resize(793, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 410))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(30, 20, 691, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 80, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)

        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(50, 110, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.label1.setFont(font)


        self.line2 = QtWidgets.QFrame(self.frame)
        self.line2.setGeometry(QtCore.QRect(50, 140, 651, 16))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line2.setLineWidth(2)

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(120, 280, 141, 41))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setFont(font)
        font.setPointSize(9)
        self.comboBox.setFont(font)

        self.privLib = QtWidgets.QRadioButton(self.frame)
        self.privLib.setGeometry(QtCore.QRect(120, 160, 141, 41))
        self.privLib.setFont(font)
        self.comLib = QtWidgets.QRadioButton(self.frame)
        self.comLib.setGeometry(QtCore.QRect(480, 160, 150, 41))
        self.comLib.setFont(font)


        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(50, 220, 651, 31))
        font.setPointSize(10)
        self.label2.setFont(font)

        self.line3 = QtWidgets.QFrame(self.frame)
        self.line3.setGeometry(QtCore.QRect(50, 250, 651, 16))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line3.setLineWidth(2)

        self.textEditIng = QtWidgets.QTextEdit(self.frame)
        self.textEditIng.setGeometry(QtCore.QRect(370, 280, 301, 41))
        font.setPointSize(9)
        self.textEditIng.setFont(font)

        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(570, 340, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/ Search Recipes"))
        self.titleLabel.setText(_translate("MainWindow", "Search Recipes"))
        self.label1.setText(_translate("MainWindow", "Search Your Private or the Community Recipe "))
        self.privLib.setText(_translate("MainWindow", "Private Library"))
        self.comLib.setText(_translate("MainWindow", "Community Library"))
        self.label2.setText(_translate("MainWindow", "Search by Recipe Name or Ingredient"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Recipe Name"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ingredient Name"))
        self.textEditIng.setHtml(_translate("MainWindow", ""))
        self.submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiSearch(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
