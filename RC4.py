# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RC4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(874, 729)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 650, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 650, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 650, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 91, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 410, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 111, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 530, 101, 31))
        self.label_5.setBaseSize(QtCore.QSize(10, 0))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 70, 581, 121))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 200, 311, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 260, 741, 141))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 420, 581, 101))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(120, 540, 581, 91))
        self.textEdit_5.setObjectName("textEdit_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RC4"))
        self.pushButton.setText(_translate("Dialog", "加密"))
        self.pushButton_2.setText(_translate("Dialog", "解密"))
        self.pushButton_3.setText(_translate("Dialog", "清空"))
        self.label.setText(_translate("Dialog", "明文"))
        self.label_2.setText(_translate("Dialog", "密文"))
        self.label_3.setText(_translate("Dialog", "密钥流"))
        self.label_4.setText(_translate("Dialog", "密钥"))
        self.label_5.setText(_translate("Dialog", "解密文"))
