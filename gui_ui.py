# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main_katashima.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 380, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 420, 131, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(180, 420, 121, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(320, 420, 121, 41))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(460, 420, 121, 41))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 380, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_1.setGeometry(QtCore.QRect(30, 480, 131, 22))
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(180, 480, 121, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(320, 480, 121, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(460, 480, 121, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.plainTextEdit_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_1.setGeometry(QtCore.QRect(30, 540, 131, 31))
        self.plainTextEdit_1.setObjectName("plainTextEdit_1")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(180, 540, 121, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(320, 540, 121, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 520, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 520, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 520, 111, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 540, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 600, 121, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(320, 600, 121, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 600, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 580, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 580, 101, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.slot1)
        self.pushButton_2.clicked.connect(MainWindow.slot2)
        self.horizontalSlider_1.valueChanged['int'].connect(MainWindow.svalue_changed)
        self.horizontalSlider_2.valueChanged['int'].connect(MainWindow.svalue_changed)
        self.horizontalSlider_3.valueChanged['int'].connect(MainWindow.svalue_changed)
        self.horizontalSlider_4.valueChanged['int'].connect(MainWindow.svalue_changed)
        self.pushButton_4.clicked.connect(MainWindow.slot4)
        self.pushButton_5.clicked.connect(MainWindow.slot5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Record"))
        self.pushButton_2.setText(_translate("MainWindow", "Valve"))
        self.label.setText(_translate("MainWindow", "dt of double pulses (ms)"))
        self.label_2.setText(_translate("MainWindow", "camera exposure (ms)"))
        self.label_3.setText(_translate("MainWindow", "laser pulse width (ms)"))
        self.pushButton_4.setText(_translate("MainWindow", "Set parameter"))
        self.pushButton_5.setText(_translate("MainWindow", "Sequence"))
        self.label_4.setText(_translate("MainWindow", "Interval (ms)"))
        self.label_5.setText(_translate("MainWindow", "Number of pairs"))

