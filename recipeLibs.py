from PyQt5 import QtCore, QtGui, QtWidgets
import removeRecipe


class Ui_MainWindow(object):
    def setupUiRecipeLibs(self, MainWindow):
        MainWindow.resize(800, 350)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        import removeRecipe
        self.removeRecipeWindow = QtWidgets.QMainWindow()
        self.removeRecipeUI = removeRecipe.Ui_MainWindow()
        self.removeRecipeUI.setupUiRemoveRec(self.removeRecipeWindow)
        self.removeRecipeWindow.hide()

        import modifyRecipe
        self.modifyRecipeWindow = QtWidgets.QMainWindow()
        self.modifyRecipeUI = modifyRecipe.Ui_MainWindow()
        self.modifyRecipeUI.setupUiModifyRecipe(self.modifyRecipeWindow)
        self.modifyRecipeWindow.hide()

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

        self.add = QtWidgets.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(50, 120, 191, 61))
        self.add.setStyleSheet("background-color: #FFFFFF;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.add.setFont(font)

        self.remove = QtWidgets.QPushButton(self.frame, clicked=self.remove)
        self.remove.setGeometry(QtCore.QRect(280, 120, 191, 61))
        self.remove.setStyleSheet("background-color: #FFFFFF;")
        self.remove.setFont(font)

        self.modify = QtWidgets.QPushButton(self.frame, clicked=self.modify)
        self.modify.setGeometry(QtCore.QRect(510, 120, 191, 61))
        self.modify.setStyleSheet("background-color: #FFFFFF;")
        self.modify.setFont(font)

        self.search1 = QtWidgets.QPushButton(self.frame)
        self.search1.setGeometry(QtCore.QRect(160, 210, 191, 61))
        self.search1.setStyleSheet("background-color: #FFFFFF;")
        self.search1.setFont(font)

        self.search2 = QtWidgets.QPushButton(self.frame)
        self.search2.setGeometry(QtCore.QRect(400, 210, 191, 61))
        self.search2.setStyleSheet("background-color: #FFFFFF;")
        self.search2.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def remove(self):
        self.removeRecipeUI.setupUiRemoveRec(self.removeRecipeWindow)
        self.removeRecipeWindow.show()

    def modify(self):
        self.modifyRecipeUI.setupUiModifyRecipe(self.modifyRecipeWindow)
        self.modifyRecipeWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library"))
        self.add.setText(_translate("MainWindow", "Add Recipe"))
        self.remove.setText(_translate("MainWindow", "Remove Recipe"))
        self.modify.setText(_translate("MainWindow", "Modify Recipe"))
        self.search1.setText(_translate("MainWindow", "Browse Your Recipes"))
        self.search2.setText(_translate("MainWindow", "Browse Community\n Recipes"))
        self.titleLabel.setText(_translate("MainWindow", "Personal and Community Library"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiRecipeLibs(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
