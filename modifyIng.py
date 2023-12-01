from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiModifyIng(self, MainWindow):
        MainWindow.resize(793, 400)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 360))
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

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitNewRecipeItem)
        self.submit.setGeometry(QtCore.QRect(570, 290, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        font.setPointSize(10)
        self.submit.setFont(font)

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

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(50, 230, 190, 41))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setFont(font)

        self.enterChange = QtWidgets.QTextEdit(self.frame)
        self.enterChange.setGeometry(QtCore.QRect(370, 230, 301, 41))
        self.enterChange.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitNewRecipeItem(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Modify Ingredient Info")
        recipeName = self.enterName.toPlainText()
        itemName = self.enterIng.toPlainText()
        newValue = self.enterChange.toPlainText()
        listedType = self.comboBox.currentText()
        x = rf.privateRecipes.loc[rf.privateRecipes["RecipeName"] == recipeName].all(1).any()
        y = rf.allIngPrivate.loc[(rf.allIngPrivate["RecipeName"] == recipeName) & (rf.allIngPrivate["ItemName"] == itemName)].all(1).any()
        if (x == True):
            if (y == True):
                if listedType == "Ingredient Name":
                    rf.updateRecipeIng(recipeName, itemName, "ItemName", newValue)
                    msg.setText("The ingredient \"" + itemName + "\" for the recipe \""
                                + recipeName + "\" has been changed to \"" + newValue + "\".")
                elif listedType == "Ingredient Quantity":
                    if newValue.isnumeric():
                        rf.updateRecipeIng(recipeName, itemName, "ItemQty", newValue)
                        msg.setText("The ingredient \"" + itemName + "\" for the recipe \""
                                    + recipeName + "\" quantity has been changed to \"" + str(newValue) + "\".")
                    else:
                        msg.setText("The item quantity you entered was not valid. Please enter a number.")
            else:
                msg.setText("The ingredient you entered is not listed as an ingredient for this recipe.")
        else:
            msg.setText("The recipe name you entered was not found in your library. ")
        msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library/ Ingredients/ Modify"))
        self.titleLabel.setText(_translate("MainWindow", "Modify an Ingredient"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.enterIng.setHtml(_translate("MainWindow", ""))
        self.enterName.setHtml(_translate("MainWindow", ""))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.ingName.setText(_translate("MainWindow", "Ingredient Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ingredient Name"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ingredient Quantity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiModifyIng(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
