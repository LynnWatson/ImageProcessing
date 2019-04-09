# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -10, 121, 571))
        self.groupBox.setObjectName("groupBox")
        self.theshSlider = QtWidgets.QSlider(self.groupBox)
        self.theshSlider.setGeometry(QtCore.QRect(10, 140, 101, 22))
        self.theshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.theshSlider.setObjectName("theshSlider")
        self.chooseImgBtn = QtWidgets.QPushButton(self.groupBox)
        self.chooseImgBtn.setGeometry(QtCore.QRect(10, 190, 101, 23))
        self.chooseImgBtn.setObjectName("chooseImgBtn")
        self.histBtn = QtWidgets.QPushButton(self.groupBox)
        self.histBtn.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.histBtn.setObjectName("histBtn")
        self.binaryBtn = QtWidgets.QPushButton(self.groupBox)
        self.binaryBtn.setGeometry(QtCore.QRect(10, 270, 101, 23))
        self.binaryBtn.setObjectName("binaryBtn")
        self.sourceView = QtWidgets.QGraphicsView(self.centralwidget)
        self.sourceView.setGeometry(QtCore.QRect(130, 40, 321, 231))
        self.sourceView.setObjectName("sourceView")
        self.histView = QtWidgets.QGraphicsView(self.centralwidget)
        self.histView.setGeometry(QtCore.QRect(460, 40, 321, 231))
        self.histView.setObjectName("histView")
        self.binaryView = QtWidgets.QGraphicsView(self.centralwidget)
        self.binaryView.setGeometry(QtCore.QRect(130, 321, 321, 231))
        self.binaryView.setObjectName("binaryView")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(460, 321, 321, 231))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(130, 10, 54, 12))
        self.Title.setObjectName("Title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 290, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 290, 54, 12))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.chooseImgBtn.setText(_translate("MainWindow", "加载源图"))
        self.histBtn.setText(_translate("MainWindow", "显示直方图"))
        self.binaryBtn.setText(_translate("MainWindow", "显示二值图"))
        self.Title.setText(_translate("MainWindow", "Source"))
        self.label.setText(_translate("MainWindow", "Histogram"))
        self.label_3.setText(_translate("MainWindow", "Binary"))
        self.label_4.setText(_translate("MainWindow", "BLANK"))

