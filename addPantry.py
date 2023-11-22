from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUiAddPantry(self, MainWindow):
        MainWindow.resize(793, 445)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 80, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(30, 20, 691, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(570, 340, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        font.setPointSize(10)
        self.submit.setFont(font)

        self.metric = QtWidgets.QRadioButton(self.frame)
        font.setPointSize(8)
        font.setBold(False)
        self.metric.setGeometry(QtCore.QRect(370, 300, 131, 20))
        self.metric.setFont(font)

        self.imperial = QtWidgets.QRadioButton(self.frame)
        self.imperial.setGeometry(QtCore.QRect(530, 300, 141, 20))
        self.imperial.setFont(font)

        self.unitType = QtWidgets.QLabel(self.frame)
        self.unitType.setGeometry(QtCore.QRect(50, 290, 311, 41))
        font.setPointSize(10)
        font.setBold(True)
        self.unitType.setFont(font)

        self.enterIng = QtWidgets.QTextEdit(self.frame)
        self.enterIng.setGeometry(QtCore.QRect(370, 170, 301, 41))
        self.enterIng.setFont(font)

        self.enterName = QtWidgets.QTextEdit(self.frame)
        self.enterName.setGeometry(QtCore.QRect(370, 110, 301, 41))
        self.enterName.setFont(font)

        self.recipeName = QtWidgets.QLabel(self.frame)
        self.recipeName.setGeometry(QtCore.QRect(50, 110, 311, 41))
        self.recipeName.setFont(font)

        self.ingName = QtWidgets.QLabel(self.frame)
        self.ingName.setGeometry(QtCore.QRect(50, 170, 311, 41))
        self.ingName.setFont(font)

        self.enterQty = QtWidgets.QTextEdit(self.frame)
        self.enterQty.setGeometry(QtCore.QRect(370, 230, 301, 41))
        self.enterQty.setFont(font)

        self.ingQty = QtWidgets.QLabel(self.frame)
        self.ingQty.setGeometry(QtCore.QRect(50, 230, 311, 41))
        self.ingQty.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Personal Pantry/ Add"))
        self.titleLabel.setText(_translate("MainWindow", "Add Pantry Item"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.metric.setText(_translate("MainWindow", "Metric"))
        self.imperial.setText(_translate("MainWindow", "Imperial"))
        self.unitType.setText(_translate("MainWindow", "Unit Type:"))
        self.enterIng.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Ingredient:</p></body></html>"))
        self.enterName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Name:</p></body></html>"))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.ingName.setText(_translate("MainWindow", "Ingredient Name"))
        self.enterQty.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Quantity:</p></body></html>"))
        self.ingQty.setText(_translate("MainWindow", "Ingredient Quantity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiAddPantry(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
