# Form implementation generated from reading ui file '/home/ake/GitHub/pyqt-test/DiceSimulatorUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 334)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.spinBoxDices = QtWidgets.QSpinBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxDices.setFont(font)
        self.spinBoxDices.setMaximum(999999999)
        self.spinBoxDices.setProperty("value", 1)
        self.spinBoxDices.setObjectName("spinBoxDices")
        self.gridLayout.addWidget(self.spinBoxDices, 0, 3, 1, 1)
        self.label3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 1, 1, 1, 2)
        self.spinBoxThrows = QtWidgets.QSpinBox(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxThrows.setFont(font)
        self.spinBoxThrows.setMaximum(999999999)
        self.spinBoxThrows.setProperty("value", 10)
        self.spinBoxThrows.setObjectName("spinBoxThrows")
        self.gridLayout.addWidget(self.spinBoxThrows, 1, 3, 1, 1)
        self.line1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 2, 1, 1, 3)
        self.label1 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 3, 1, 1, 1)
        self.lcdNumberDiceOutcome = QtWidgets.QLCDNumber(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumberDiceOutcome.setFont(font)
        self.lcdNumberDiceOutcome.setDigitCount(10)
        self.lcdNumberDiceOutcome.setObjectName("lcdNumberDiceOutcome")
        self.gridLayout.addWidget(self.lcdNumberDiceOutcome, 3, 2, 1, 2)
        self.line2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 5, 1, 1, 3)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.lcdNumberActualThrows = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumberActualThrows.setDigitCount(10)
        self.lcdNumberActualThrows.setObjectName("lcdNumberActualThrows")
        self.gridLayout.addWidget(self.lcdNumberActualThrows, 4, 2, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonStart = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttonStart.setObjectName("buttonStart")
        self.horizontalLayout.addWidget(self.buttonStart)
        self.buttonStop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttonStop.setObjectName("buttonStop")
        self.horizontalLayout.addWidget(self.buttonStop)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 3)
        self.line1.raise_()
        self.label3.raise_()
        self.spinBoxThrows.raise_()
        self.label2.raise_()
        self.label1.raise_()
        self.lcdNumberDiceOutcome.raise_()
        self.line2.raise_()
        self.spinBoxDices.raise_()
        self.lcdNumberActualThrows.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dice Simulator"))
        self.label2.setText(_translate("MainWindow", "Number of dices"))
        self.label3.setText(_translate("MainWindow", "Dice throws per second"))
        self.label1.setText(_translate("MainWindow", "Dice sum"))
        self.label.setText(_translate("MainWindow", "Actual throws/s"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.buttonStop.setText(_translate("MainWindow", "Stop"))
