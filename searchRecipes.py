from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUiSearch(self, MainWindow):
        MainWindow.resize(793, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 461))
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

        self.searchIng = QtWidgets.QRadioButton(self.frame)
        self.searchIng.setGeometry(QtCore.QRect(120, 280, 141, 41))
        font.setPointSize(9)
        self.searchIng.setFont(font)
        self.privLib = QtWidgets.QRadioButton(self.frame)
        self.privLib.setGeometry(QtCore.QRect(120, 160, 141, 41))
        self.privLib.setFont(font)
        self.searchName = QtWidgets.QRadioButton(self.frame)
        self.searchName.setGeometry(QtCore.QRect(120, 350, 171, 41))
        self.searchName.setFont(font)
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

        self.textEditName = QtWidgets.QTextEdit(self.frame)
        self.textEditName.setGeometry(QtCore.QRect(370, 350, 301, 41))
        self.textEditName.setFont(font)

        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(570, 400, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/ Search Recipes"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to Personal Cookbook"))
        self.label1.setText(_translate("MainWindow", "Search Your Private or the Community Recipe "))
        self.searchIng.setText(_translate("MainWindow", "Search Ingredient"))
        self.privLib.setText(_translate("MainWindow", "Private Library"))
        self.searchName.setText(_translate("MainWindow", "Search Recipe Name"))
        self.comLib.setText(_translate("MainWindow", "Community Library"))
        self.label2.setText(_translate("MainWindow", "Search by Recipe Name or Ingredient"))
        self.textEditIng.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Ingredient: </p></body></html>"))
        self.textEditName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Name:</p></body></html>"))
        self.submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiSearch(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
