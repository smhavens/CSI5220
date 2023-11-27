from PyQt5 import QtCore, QtGui, QtWidgets
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiAllRecipeIng(self, MainWindow):
        MainWindow.resize(800, 350)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        import addRecipeItem
        self.addRecipeItemWindow = QtWidgets.QMainWindow()
        self.addRecipeItemUI = addRecipeItem.Ui_MainWindow()
        self.addRecipeItemUI.setupUiAddRecipeIng(self.addRecipeItemWindow)
        self.addRecipeItemWindow.hide()

        import removeIng
        self.removeIngWindow = QtWidgets.QMainWindow()
        self.removeIngUI = removeIng.Ui_MainWindow()
        self.removeIngUI.setupUiRemoveRecipeIng(self.removeIngWindow)
        self.removeIngWindow.hide()

        import browsePubIng
        temp = rf.allIngPrivate
        self.ingWindow = QtWidgets.QMainWindow()
        self.ingUI = browsePubIng.Ui_MainWindow()
        self.ingUI.setupUiBrowsePrivPub(self.ingWindow, temp)
        self.ingWindow.hide()

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 311))
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

        self.add = QtWidgets.QPushButton(self.frame, clicked=self.addRecipeIng)
        self.add.setGeometry(QtCore.QRect(50, 120, 191, 61))
        self.add.setStyleSheet("background-color: #FFFFFF;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.add.setFont(font)

        self.removeIng = QtWidgets.QPushButton(self.frame, clicked=self.removeRecipeIng)
        self.removeIng.setGeometry(QtCore.QRect(280, 120, 191, 61))
        self.removeIng.setStyleSheet("background-color: #FFFFFF;")
        self.removeIng.setFont(font)

        self.modifyIng = QtWidgets.QPushButton(self.frame)
        self.modifyIng.setGeometry(QtCore.QRect(510, 120, 191, 61))
        self.modifyIng.setStyleSheet("background-color: #FFFFFF;")
        self.modifyIng.setFont(font)

        self.unitType = QtWidgets.QPushButton(self.frame)
        self.unitType.setGeometry(QtCore.QRect(50, 210, 191, 61))
        self.unitType.setStyleSheet("background-color: #FFFFFF;")
        self.unitType.setFont(font)

        self.search1 = QtWidgets.QPushButton(self.frame, clicked=self.browsePrivIng)
        self.search1.setGeometry(QtCore.QRect(280, 210, 191, 61))
        self.search1.setStyleSheet("background-color: #FFFFFF;")
        self.search1.setFont(font)

        self.search2 = QtWidgets.QPushButton(self.frame, clicked=self.browsePubIng)
        self.search2.setGeometry(QtCore.QRect(510, 210, 191, 61))
        self.search2.setStyleSheet("background-color: #FFFFFF;")
        self.search2.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addRecipeIng(self):
        self.addRecipeItemUI.setupUiAddRecipeIng(self.addRecipeItemWindow)
        self.addRecipeItemWindow.show()

    def removeRecipeIng(self):
        self.removeIngUI.setupUiRemoveRecipeIng(self.removeIngWindow)
        self.removeIngWindow.show()

    def browsePrivIng(self):
        temp = rf.allIngPrivate
        self.ingUI.setupUiBrowsePrivPub(self.ingWindow, temp)
        self.ingWindow.show()

    def browsePubIng(self):
        temp = rf.allIngPublic
        self.ingUI.setupUiBrowsePrivPub(self.ingWindow, temp)
        self.ingWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library/Recipe Ingredients"))
        self.add.setText(_translate("MainWindow", "Add Ingredient"))
        self.removeIng.setText(_translate("MainWindow", "Remove Ingredient"))
        self.modifyIng.setText(_translate("MainWindow", "Modify Ingredient"))
        self.unitType.setText(_translate("MainWindow", "Switch Ingredient\nUnit Type"))
        self.search1.setText(_translate("MainWindow", "Browse Your\nRecipe Ingredients"))
        self.search2.setText(_translate("MainWindow", "Browse Community\nRecipes Ingredients"))
        self.titleLabel.setText(_translate("MainWindow", "Personal and Community Recipe Ingredients"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiAllRecipeIng(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
