from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiAddRecipe(self, MainWindow):
        MainWindow.resize(793, 511)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 471))
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

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitNewRecipe)
        self.submit.setGeometry(QtCore.QRect(570, 400, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        font.setPointSize(10)
        self.submit.setFont(font)

        self.yesRB = QtWidgets.QRadioButton(self.frame)
        self.yesRB.setGeometry(QtCore.QRect(370, 360, 131, 20))

        self.noRB = QtWidgets.QRadioButton(self.frame)
        self.noRB.setGeometry(QtCore.QRect(530, 360, 141, 20))
        self.noRB.setChecked(True)

        self.isPublic = QtWidgets.QLabel(self.frame)
        self.isPublic.setGeometry(QtCore.QRect(50, 350, 311, 41))
        font.setPointSize(10)
        font.setBold(True)
        self.isPublic.setFont(font)

        self.enterInstructions = QtWidgets.QTextEdit(self.frame)
        self.enterInstructions.setGeometry(QtCore.QRect(370, 170, 301, 41))
        self.enterInstructions.setFont(font)

        self.enterName = QtWidgets.QTextEdit(self.frame)
        self.enterName.setGeometry(QtCore.QRect(370, 110, 301, 41))
        self.enterName.setFont(font)

        self.recipeName = QtWidgets.QLabel(self.frame)
        self.recipeName.setGeometry(QtCore.QRect(50, 110, 311, 41))
        self.recipeName.setFont(font)

        self.instructions = QtWidgets.QLabel(self.frame)
        self.instructions.setGeometry(QtCore.QRect(50, 170, 311, 41))
        self.instructions.setFont(font)

        self.enterServ = QtWidgets.QTextEdit(self.frame)
        self.enterServ.setGeometry(QtCore.QRect(370, 230, 301, 41))
        self.enterServ.setFont(font)

        self.servings = QtWidgets.QLabel(self.frame)
        self.servings.setGeometry(QtCore.QRect(50, 230, 311, 41))
        self.servings.setFont(font)

        self.enterDesc = QtWidgets.QTextEdit(self.frame)
        self.enterDesc.setGeometry(QtCore.QRect(370, 290, 301, 41))
        self.enterDesc.setFont(font)

        self.recipeDesc = QtWidgets.QLabel(self.frame)
        self.recipeDesc.setGeometry(QtCore.QRect(50, 290, 311, 41))
        self.recipeDesc.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitNewRecipe(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Add New Recipe Info")
        recipeName = self.enterName.toPlainText()
        recipeServings = self.enterServ.toPlainText()
        recipeDesc = self.enterDesc.toPlainText()
        recipeSteps = self.enterInstructions.toPlainText()
        isPublic = self.yesRB.isChecked()
        if recipeServings.isdigit():
            rf.addPrivateRecipe(recipeName, recipeSteps, recipeServings, recipeDesc, isPublic)
            if (isPublic == False):
                msg.setText("The recipe \"" + recipeName + "\" has been added to your private library.")
            else:
                msg.setText("The recipe \"" + recipeName + "\" has been added to your private library and the public "
                                                           "community library.")
        else:
            msg.setText("The servings quantity you entered was not valid. Please enter a whole number.")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Personal Pantry/Add Recipe"))
        self.titleLabel.setText(_translate("MainWindow", "Add Recipe"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.yesRB.setText(_translate("MainWindow", "Yes"))
        self.noRB.setText(_translate("MainWindow", "No"))
        self.isPublic.setText(_translate("MainWindow", "Add to Community Library:"))
        self.enterInstructions.setHtml(_translate("MainWindow", ""))
        self.enterName.setHtml(_translate("MainWindow", ""))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.instructions.setText(_translate("MainWindow", "Instructions:"))
        self.enterServ.setHtml(_translate("MainWindow", ""))
        self.servings.setText(_translate("MainWindow", "Servings:"))
        self.enterDesc.setHtml(_translate("MainWindow", ""))
        self.recipeDesc.setText(_translate("MainWindow", "Recipe Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiAddRecipe(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
