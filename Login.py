# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Sat Jul 12 17:40:37 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(369, 230)
        self.verticalLayoutWidget = QtGui.QWidget(Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 221, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nombreu = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nombreu.setObjectName("nombreu")
        self.verticalLayout.addWidget(self.nombreu)
        self.contrase = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.contrase.setEchoMode(QtGui.QLineEdit.Password)
        self.contrase.setObjectName("contrase")
        self.verticalLayout.addWidget(self.contrase)
        self.horizontalLayoutWidget = QtGui.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 130, 241, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Aceptar = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Aceptar.setAutoDefault(True)
        self.Aceptar.setDefault(True)
        self.Aceptar.setFlat(False)
        self.Aceptar.setObjectName("Aceptar")
        self.horizontalLayout.addWidget(self.Aceptar)
        self.Cancelar = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Cancelar.setObjectName("Cancelar")
        self.horizontalLayout.addWidget(self.Cancelar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.nombreu.setPlaceholderText(QtGui.QApplication.translate("Login", "Escriba nombre de usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.contrase.setPlaceholderText(QtGui.QApplication.translate("Login", "Escriba su contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.Aceptar.setText(QtGui.QApplication.translate("Login", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancelar.setText(QtGui.QApplication.translate("Login", "Cancelar ", None, QtGui.QApplication.UnicodeUTF8))

