from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUiHomePage(self, MainWindow):
        # specifying UI screen size
        MainWindow.resize(800, 370)
        # personalizing UI screen
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        # creating UI screen
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # adding a frame to the UI screen
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 331))
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

        self.pantry = QtWidgets.QPushButton(self.frame, clicked=self.pantry)
        self.pantry.setGeometry(QtCore.QRect(420, 110, 251, 71))
        self.pantry.setStyleSheet("background-color: #6eb4e0;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.pantry.setFont(font)

        self.recipes = QtWidgets.QPushButton(self.frame, clicked=self.recipeLib)
        self.recipes.setGeometry(QtCore.QRect(80, 110, 251, 71))
        self.recipes.setStyleSheet("background-color: #6eb4e0;")
        self.recipes.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.search = QtWidgets.QPushButton(self.frame, clicked=self.search)
        self.search.setGeometry(QtCore.QRect(251, 210, 251, 71))
        self.search.setStyleSheet("background-color: #6eb4e0;")
        self.search.setFont(font)

        # self.mealPlan = QtWidgets.QPushButton(self.frame, clicked=self.mealPlan)
        # self.mealPlan.setGeometry(QtCore.QRect(420, 210, 251, 71))
        # self.mealPlan.setStyleSheet("background-color: #FFFFFF;")
        # self.mealPlan.setFont(font)

        self.namesLabel = QtWidgets.QLabel(self.frame)
        self.namesLabel.setGeometry(QtCore.QRect(30, 295, 691, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.namesLabel.setFont(font)
        self.namesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namesLabel.setObjectName("namesLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def recipeLib(self):
        import recipeLibs
        self.recipeLibsWindow = QtWidgets.QMainWindow()
        self.recipeLibsUI = recipeLibs.Ui_MainWindow()
        self.recipeLibsUI.setupUiRecipeLibs(self.recipeLibsWindow)
        # MainWindow.close()
        self.recipeLibsWindow.show()

    def pantry(self):
        import personalPantry
        self.pantryWindow = QtWidgets.QMainWindow()
        self.pantryUI = personalPantry.Ui_MainWindow()
        self.pantryUI.setupUiPantry(self.pantryWindow)
        # MainWindow.close()
        self.pantryWindow.show()

    def search(self):
        import searchRecipes
        self.searchWindow = QtWidgets.QMainWindow()
        self.searchUI = searchRecipes.Ui_MainWindow()
        self.searchUI.setupUiSearch(self.searchWindow)
        # MainWindow.close()
        self.searchWindow.show()

    # def mealPlan(self):
    #     import mealPlan
    #     self.mealPlanWindow = QtWidgets.QMainWindow()
    #     self.mealPlanUI = mealPlan.Ui_MainWindow()
    #     self.mealPlanUI.setupUiMP(self.mealPlanWindow)
    #     # MainWindow.close()
    #     self.mealPlanWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/ Home"))
        self.titleLabel.setText(_translate("MainWindow", "Welcome to Personal Cookbook"))
        self.pantry.setText(_translate("MainWindow", "Personal Pantry"))
        self.search.setText(_translate("MainWindow", "Search Recipes"))
        # self.mealPlan.setText(_translate("MainWindow", "Create Meal Plan"))
        self.recipes.setText(_translate("MainWindow", "Recipe Libraries"))
        self.namesLabel.setText(_translate("MainWindow", "Created by: Denise Rauschendorfer & Mila Havens"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiHomePage(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
