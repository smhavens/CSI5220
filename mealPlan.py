from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiMP(self, MainWindow):
        MainWindow.resize(793, 480)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        import shoppingList
        self.shoppingListWindow = QtWidgets.QMainWindow()
        self.shoppingListUI = shoppingList.Ui_MainWindow()
        self.shoppingListUI.setupUiShoppingList(self.shoppingListWindow)
        self.shoppingListWindow.hide()

        import browseMP
        self.browseMPWindow = QtWidgets.QMainWindow()
        self.browseMPUI = browseMP.Ui_MainWindow()
        self.browseMPUI.setupUiBrowseMP(self.browseMPWindow)
        self.browseMPWindow.hide()

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 441))
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

        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(50, 110, 651, 31))
        font.setPointSize(10)
        self.label1.setFont(font)

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(50, 140, 651, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)

        self.metricRB = QtWidgets.QRadioButton(self.frame)
        self.metricRB.setGeometry(QtCore.QRect(370, 320, 141, 41))
        font.setPointSize(9)
        font.setBold(False)
        self.metricRB.setFont(font)

        self.imperialRB = QtWidgets.QRadioButton(self.frame)
        self.imperialRB.setGeometry(QtCore.QRect(530, 320, 141, 41))
        self.imperialRB.setFont(font)
        self.imperialRB.setChecked(True)

        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(50, 180, 311, 41))
        font.setPointSize(10)
        font.setBold(True)
        self.label2.setFont(font)

        self.textEditName = QtWidgets.QTextEdit(self.frame)
        self.textEditName.setGeometry(QtCore.QRect(370, 180, 301, 41))
        self.textEditName.setFont(font)

        self.textEditSev = QtWidgets.QTextEdit(self.frame)
        self.textEditSev.setGeometry(QtCore.QRect(370, 250, 301, 41))
        self.textEditSev.setFont(font)

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.addToMealPlan)
        self.submit.setGeometry(QtCore.QRect(570, 370, 150, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        self.viewMP = QtWidgets.QPushButton(self.frame, clicked=self.browseMP)
        self.viewMP.setGeometry(QtCore.QRect(50, 370, 150, 51))
        self.viewMP.setStyleSheet("background-color: #61d800;")
        self.viewMP.setFont(font)

        self.clear = QtWidgets.QPushButton(self.frame, clicked=self.clearMP)
        self.clear.setGeometry(QtCore.QRect(225, 370, 150, 51))
        self.clear.setStyleSheet("background-color: #61d800;")
        self.clear.setFont(font)

        self.shopping = QtWidgets.QPushButton(self.frame, clicked=self.viewShoppingList)
        self.shopping.setGeometry(QtCore.QRect(395, 370, 150, 51))
        self.shopping.setStyleSheet("background-color: #61d800;")
        self.shopping.setFont(font)

        self.label3 = QtWidgets.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(50, 250, 311, 41))
        self.label3.setFont(font)

        self.label4 = QtWidgets.QLabel(self.frame)
        self.label4.setGeometry(QtCore.QRect(50, 320, 311, 41))
        self.label4.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def viewShoppingList(self):
        rf.groceryList()
        self.shoppingListUI.setupUiShoppingList(self.shoppingListWindow)
        self.shoppingListWindow.show()

    def clearMP(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Meal Plan Info")
        rf.clearMealPlan()
        msg.setText("Your meal plan has been cleared.")
        msg.exec_()


    def browseMP(self):
        self.browseMPUI.setupUiBrowseMP(self.browseMPWindow)
        self.browseMPWindow.show()


    def addToMealPlan(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Meal Plan Info")
        isImperial = self.imperialRB.isChecked()
        recipeName = self.textEditName.toPlainText()
        servings = self.textEditSev.toPlainText()
        rf.viewAll(rf.mealPlan)
        x = rf.privateRecipes.loc[rf.privateRecipes["RecipeName"] == recipeName].all().any()
        print(rf.privateRecipes.loc[rf.privateRecipes["RecipeName"] == recipeName].all())
        print(x)
        if (x == True):
            if (rf.mealPlan.loc[rf.mealPlan["RecipeName"] == recipeName]).all().any() == False:
                if (servings.isnumeric()):
                    rf.addRecipeToMealPlan(rf.privateRecipes, rf.allIngPrivate, recipeName)
                    rf.changeServings(recipeName, servings)
                    if (isImperial == True):
                        rf.unitChange(recipeName, "Imperial")
                    else:
                        rf.unitChange(recipeName, "Metric")
                    msg.setText("The recipe \"" + recipeName + "\" has been added to your meal plan.")
                else:
                    msg.setText("The servings quantity you entered was not valid. Please enter a number.")
            else:
                msg.setText("This recipe is already in your meal plan.")
        else:
            msg.setText("The recipe name you entered was not found in your library. "
                        "You can only add recipes to your meal plan that are in your library.")
        msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/ Meal Plan"))
        self.titleLabel.setText(_translate("MainWindow", "Create Meal Plan"))
        self.label1.setText(_translate("MainWindow", "Enter the Recipes You Want to Make"))
        self.metricRB.setText(_translate("MainWindow", "Metric"))
        self.imperialRB.setText(_translate("MainWindow", "Imperial"))
        self.label2.setText(_translate("MainWindow", "Recipe Name:"))
        self.textEditName.setHtml(_translate("MainWindow", ""))
        self.textEditSev.setHtml(_translate("MainWindow", ""))
        self.submit.setText(_translate("MainWindow", "Add to Meal Plan"))
        self.clear.setText(_translate("MainWindow", "Clear Meal Plan"))
        self.viewMP.setText(_translate("MainWindow", "View Meal Plan"))
        self.shopping.setText(_translate("MainWindow", "Shopping List"))
        self.label3.setText(_translate("MainWindow", "Desired Serving Size: "))
        self.label4.setText(_translate("MainWindow", "Desired Units: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiMP(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
