from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiRemoveRecipeIng(self, MainWindow):
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

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitRemPantry)
        self.submit.setGeometry(QtCore.QRect(570, 255, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        self.recipeLib = QtWidgets.QLabel(self.frame)
        self.recipeLib.setGeometry(QtCore.QRect(50, 200, 311, 41))
        self.recipeLib.setFont(font)

        self.textEdit2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit2.setGeometry(QtCore.QRect(370, 200, 301, 41))
        self.textEdit2.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitRemPantry(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Remove Ingredient Info")
        recipeName = self.textEdit.toPlainText()
        recipeIngredient = self.textEdit2.toPlainText()
        y = rf.privateRecipes.loc[rf.privateRecipes["RecipeName"] == recipeName].all().any()
        if (y == True):
            if (rf.allIngPublic.loc[(rf.allIngPublic["RecipeName"] == recipeName) & (rf.allIngPublic["ItemName"] == recipeIngredient)]).all().any() == True:
                rf.removeRecipeIng(recipeName, recipeIngredient)
                msg.setText("The ingredient \"" + recipeIngredient + "\" has been removed from \"" + recipeName + "\".")
            else:
                msg.setText("The ingredient you entered is not listed for this recipe.")
        else:
            msg.setText("The recipe you entered was not found in your library.")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library/ Ingredients/ Remove"))
        self.titleLabel.setText(_translate("MainWindow", "Remove an Ingredient"))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.textEdit.setHtml(_translate("MainWindow", ""))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.recipeLib.setText(_translate("MainWindow", "Recipe Ingredient:"))
        self.textEdit2.setHtml(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiRemoveRecipeIng(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
