# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dvi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#code by yangchuqiao in 20201118

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(80, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(260, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 124, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 40, 231, 174))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text1 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.text1.setObjectName("text1")
        self.verticalLayout_2.addWidget(self.text1)
        self.text2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.text2.setObjectName("text2")
        self.verticalLayout_2.addWidget(self.text2)
        self.text3 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.text3.setObjectName("text3")
        self.verticalLayout_2.addWidget(self.text3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 20, 81, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.path1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path1.setFont(font)
        self.path1.setObjectName("path1")
        self.verticalLayout_3.addWidget(self.path1)
        self.path1.clicked.connect(self.showDialog1)  # 医学影像源路径

        self.path2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path2.setFont(font)
        self.path2.setObjectName("path2")
        self.verticalLayout_3.addWidget(self.path2)
        self.path3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path3.setFont(font)
        self.path3.setObjectName("path3")
        self.verticalLayout_3.addWidget(self.path3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "医学影像简易处理工具"))
        self.start.setText(_translate("MainWindow", "处理"))
        self.clear.setText(_translate("MainWindow", "重置"))
        self.label1.setText(_translate("MainWindow", "医学影像数据源位置："))
        self.label2.setText(_translate("MainWindow", "处理后图像保存位置："))
        self.label3.setText(_translate("MainWindow", "处理后文档保存位置："))
        self.path1.setText(_translate("MainWindow", "选择路径"))
        self.path2.setText(_translate("MainWindow", "选择路径"))
        self.path3.setText(_translate("MainWindow", "选择路径"))

    def showDialog1(self, MainWindow):
        directory1 = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹",  "./",None, QtWidgets.QFileDialog.DontUseNativeDialog)
        print(directory1)
        self.text1.setText(directory1)



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

