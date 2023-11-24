from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiAddPantry(self, MainWindow):
        MainWindow.resize(793, 435)
        MainWindow.setStyleSheet("background-color: #123456;")
        MainWindow.setWindowIcon(QtGui.QIcon('chef.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 395))
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

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitNewPantry)
        self.submit.setGeometry(QtCore.QRect(570, 330, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        font.setPointSize(10)
        self.submit.setFont(font)

        self.metric = QtWidgets.QRadioButton(self.frame)
        font.setPointSize(8)
        font.setBold(False)
        self.metric.setGeometry(QtCore.QRect(370, 290, 131, 20))
        self.metric.setFont(font)

        self.imperial = QtWidgets.QRadioButton(self.frame)
        self.imperial.setGeometry(QtCore.QRect(490, 290, 141, 20))
        self.imperial.setFont(font)

        self.other = QtWidgets.QRadioButton(self.frame)
        self.other.setGeometry(QtCore.QRect(610, 290, 91, 20))
        self.other.setFont(font)
        self.other.setChecked(True)

        self.unitType = QtWidgets.QLabel(self.frame)
        self.unitType.setGeometry(QtCore.QRect(50, 290, 311, 41))
        font.setPointSize(10)
        font.setBold(True)
        self.unitType.setFont(font)

        self.enterIng = QtWidgets.QTextEdit(self.frame)
        self.enterIng.setGeometry(QtCore.QRect(370, 110, 301, 41))
        self.enterIng.setFont(font)

        self.ingName = QtWidgets.QLabel(self.frame)
        self.ingName.setGeometry(QtCore.QRect(50, 110, 311, 41))
        self.ingName.setFont(font)

        self.enterQty = QtWidgets.QTextEdit(self.frame)
        self.enterQty.setGeometry(QtCore.QRect(370, 170, 301, 41))
        self.enterQty.setFont(font)

        self.ingQty = QtWidgets.QLabel(self.frame)
        self.ingQty.setGeometry(QtCore.QRect(50, 170, 311, 41))
        self.ingQty.setFont(font)

        self.enterUnits = QtWidgets.QTextEdit(self.frame)
        self.enterUnits.setGeometry(QtCore.QRect(370, 230, 301, 41))
        self.enterUnits.setFont(font)

        self.ingUnits = QtWidgets.QLabel(self.frame)
        self.ingUnits.setGeometry(QtCore.QRect(50, 230, 311, 41))
        self.ingUnits.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitNewPantry(self):
        validImperial = ["oz (liquid)", "oz (dry)", "cups (liquid)", "Tbsp", "tsp"]
        validMetric = ["mL", "g", "dsp"]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('chef.png'))
        msg.setWindowTitle("Add Pantry Item Info")
        itemName = self.enterIng.toPlainText()
        itemQty = self.enterQty.toPlainText()
        itemUnits = self.enterUnits.toPlainText()
        isMetric = self.metric.isChecked()
        isImperial = self.imperial.isChecked()
        x = rf.pantry.loc[rf.pantry["ItemName"] == itemName].all(1).any()
        if (x == False):
            if (itemQty.isnumeric()):
                if (isImperial == True):
                    if (itemUnits in validImperial):
                        rf.addPantryItem(itemName, itemQty, itemUnits, "Imperial")
                        msg.setText("The ingredient \"" + itemName +
                                    "\" has been added to your pantry with the quantity \"" + str(itemQty) +
                                    " " + itemUnits + ".")
                    else:
                        msg.setText("The units you entered are not in our supported list of valid imperial units. "
                                    "Please convert this item to one of the following unit measurements:"
                                    "\n\t1. oz (liquid)\n\t2. oz (dry)\n\t3. cups (liquid)\n\t4. Tbsp\n\t5. tsp")

                elif (isMetric == True):
                    if (itemUnits in validMetric):
                        rf.addPantryItem(itemName, itemQty, itemUnits, "Metric")
                        msg.setText("The ingredient \"" + itemName +
                                    "\" has been added to your pantry with the quantity \"" + str(itemQty) +
                                    " " + itemUnits + ".")
                    else:
                        msg.setText("The units you entered are not in our supported list of valid metric units. "
                                    "Please convert this item to one of the following unit measurements:"
                                    "\n\t1. mL\n\t2. g\n\t3. dsp")
                else:
                    rf.addPantryItem(itemName, itemQty, itemUnits, "Other")
                    msg.setText("The ingredient \"" + itemName +
                                "\" has been added to your pantry with the quantity \"" + str(itemQty) +
                                " " + itemUnits + ".\n Please note that this item will not be affected if you "
                                                  "decide to convert the recipe to either metric or "
                                                  "imperial units.")
            else:
                msg.setText("The pantry item quantity you entered was not valid. Please enter a number.")
        else:
            msg.setText("The pantry item you entered is already in you pantry.")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Personal Pantry/ Add Pantry"))
        self.titleLabel.setText(_translate("MainWindow", "Add Pantry Item"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.metric.setText(_translate("MainWindow", "Metric"))
        self.imperial.setText(_translate("MainWindow", "Imperial"))
        self.other.setText(_translate("MainWindow", "Other"))
        self.unitType.setText(_translate("MainWindow", "Unit Type:"))
        self.enterIng.setHtml(_translate("MainWindow", ""))
        self.ingName.setText(_translate("MainWindow", "Ingredient Name:"))
        self.enterQty.setHtml(_translate("MainWindow", ""))
        self.ingQty.setText(_translate("MainWindow", "Ingredient Quantity:"))
        self.ingUnits.setText(_translate("MainWindow", "Ingredient Units:"))
        self.enterUnits.setHtml(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiAddPantry(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
