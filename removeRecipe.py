from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiRemoveRec(self, MainWindow):
        MainWindow.resize(793, 360)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 321))
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

        self.recipeName = QtWidgets.QLabel(self.frame)
        self.recipeName.setGeometry(QtCore.QRect(50, 130, 311, 41))
        font.setPointSize(10)
        self.recipeName.setFont(font)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(370, 130, 301, 41))
        self.textEdit.setFont(font)

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitRemoveRecipe)
        self.submit.setGeometry(QtCore.QRect(570, 250, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        self.recipeLib = QtWidgets.QLabel(self.frame)
        self.recipeLib.setGeometry(QtCore.QRect(50, 200, 311, 41))
        self.recipeLib.setFont(font)

        self.privateCB = QtWidgets.QRadioButton(self.frame)
        font.setPointSize(8)
        font.setBold(False)
        self.privateCB.setGeometry(QtCore.QRect(370, 200, 121, 41))
        self.privateCB.setChecked(True)
        self.privateCB.setFont(font)

        self.publicCB = QtWidgets.QRadioButton(self.frame)
        self.publicCB.setGeometry(QtCore.QRect(530, 200, 141, 41))
        self.publicCB.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitRemoveRecipe(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Remove Recipe Info")
        recipeName = self.textEdit.toPlainText()
        x = self.privateCB.isChecked()
        y = rf.privateRecipes.loc[rf.privateRecipes["RecipeName"] == recipeName].all(1).any()
        if (x == True) and (y == True):
            rf.removePublicRecipe(recipeName)
            msg.setText("The recipe \"" + recipeName + "\" has been removed from your Private Library "
                                                       "and the Public Community Library.")
        elif (x == False) and (y == True):
            rf.removePublicRecipe(recipeName)
            msg.setText("The recipe \"" + recipeName + "\" has been removed from the public Community Library.")
        else:
            msg.setText("The recipe name you entered was not found in the library specified.")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library/ Remove"))
        self.titleLabel.setText(_translate("MainWindow", "Remove a Recipe"))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.textEdit.setHtml(_translate("MainWindow", ""))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.recipeLib.setText(_translate("MainWindow", "Recipe Library:"))
        self.privateCB.setText(_translate("MainWindow", "Private Library"))
        self.publicCB.setText(_translate("MainWindow", "Community Library"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiRemoveRec(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
