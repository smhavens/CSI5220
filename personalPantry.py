from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUiPantry(self, MainWindow):
        MainWindow.resize(800, 350)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        import addPantry
        self.addPantryWindow = QtWidgets.QMainWindow()
        self.addPantryUI = addPantry.Ui_MainWindow()
        self.addPantryUI.setupUiAddPantry(self.addPantryWindow)
        self.addPantryWindow.hide()

        import removePantry
        self.removePantryWindow = QtWidgets.QMainWindow()
        self.removePantryUI = removePantry.Ui_MainWindow()
        self.removePantryUI.setupUiRemovePantry(self.removePantryWindow)
        self.removePantryWindow.hide()

        import browsePantry
        self.browsePantryWindow = QtWidgets.QMainWindow()
        self.browsePantryUI = browsePantry.Ui_MainWindow()
        self.browsePantryUI.setupUiBrowsePantry(self.browsePantryWindow)
        self.browsePantryWindow.hide()

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 311))
        self.frame.setStyleSheet("background-color: white;")
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

        self.add = QtWidgets.QPushButton(self.frame, clicked=self.addPantry)
        self.add.setGeometry(QtCore.QRect(80, 110, 251, 71))
        self.add.setStyleSheet("background-color: #FFFFFF;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.add.setFont(font)

        self.remove = QtWidgets.QPushButton(self.frame, clicked=self.remove)
        self.remove.setGeometry(QtCore.QRect(420, 110, 251, 71))
        self.remove.setStyleSheet("background-color: #FFFFFF;")
        self.remove.setFont(font)

        self.modify = QtWidgets.QPushButton(self.frame)
        self.modify.setGeometry(QtCore.QRect(80, 210, 251, 71))
        self.modify.setStyleSheet("background-color: #FFFFFF;")
        self.modify.setFont(font)

        self.browse = QtWidgets.QPushButton(self.frame, clicked=self.browse)
        self.browse.setGeometry(QtCore.QRect(420, 210, 251, 71))
        self.browse.setStyleSheet("background-color: #FFFFFF;")
        self.browse.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addPantry(self):
        self.addPantryUI.setupUiAddPantry(self.addPantryWindow)
        self.addPantryWindow.show()

    def remove(self):
        self.removePantryUI.setupUiRemovePantry(self.removePantryWindow)
        self.removePantryWindow.show()

    def browse(self):
        self.browsePantryUI.setupUiBrowsePantry(self.browsePantryWindow)
        self.browsePantryWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Personal Pantry"))
        self.titleLabel.setText(_translate("MainWindow", "Personal Pantry"))
        self.add.setText(_translate("MainWindow", "Add Ingredient"))
        self.remove.setText(_translate("MainWindow", "Remove Ingredient"))
        self.modify.setText(_translate("MainWindow", "Modify Ingredient"))
        self.browse.setText(_translate("MainWindow", "Browse Pantry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiPantry(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
