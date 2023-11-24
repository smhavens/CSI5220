from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import recipeFuncs as rf


class Ui_MainWindow(object):
    def setupUiModifyRecipe(self, MainWindow):
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

        self.submit = QtWidgets.QPushButton(self.frame, clicked=self.submitxxxx)
        self.submit.setGeometry(QtCore.QRect(570, 250, 161, 51))
        self.submit.setStyleSheet("background-color: #61d800;")
        self.submit.setFont(font)

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(50, 190, 141, 41))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setFont(font)

        self.newVal = QtWidgets.QTextEdit(self.frame)
        self.newVal.setGeometry(QtCore.QRect(370, 190, 301, 41))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submitxxxx(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowIcon(QtGui.QIcon('chef.png'))
        self.msg.setWindowTitle("Pantry Item Removed")
        self.msg.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Cookbook/Recipe Library/ Modify"))
        self.titleLabel.setText(_translate("MainWindow", "Modify a Recipe"))
        self.recipeName.setText(_translate("MainWindow", "Recipe Name:"))
        self.textEdit.setHtml(_translate("MainWindow", ""))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "RecipeName"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Instructions"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Servings"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Description"))
        self.newVal.setHtml(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiModifyRecipe(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
