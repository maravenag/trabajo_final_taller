# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarImagen.ui'
#
# Created: Tue May 27 11:34:29 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditarImagen(object):
    def setupUi(self, EditarImagen):
        EditarImagen.setObjectName("EditarImagen")
        EditarImagen.resize(355, 443)
        self.verticalLayoutWidget = QtGui.QWidget(EditarImagen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 40, 191, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img = QtGui.QLabel(self.verticalLayoutWidget)
        self.img.setText("")
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.verticalLayout.addWidget(self.img)
        self.Cambiar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Cambiar.setObjectName("Cambiar")
        self.verticalLayout.addWidget(self.Cambiar)
        self.horizontalLayoutWidget = QtGui.QWidget(EditarImagen)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 380, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Cancelar = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Cancelar.setObjectName("Cancelar")
        self.horizontalLayout.addWidget(self.Cancelar)
        self.Aceptar = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Aceptar.setObjectName("Aceptar")
        self.horizontalLayout.addWidget(self.Aceptar)

        self.retranslateUi(EditarImagen)
        QtCore.QMetaObject.connectSlotsByName(EditarImagen)

    def retranslateUi(self, EditarImagen):
        EditarImagen.setWindowTitle(QtGui.QApplication.translate("EditarImagen", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Cambiar.setText(QtGui.QApplication.translate("EditarImagen", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancelar.setText(QtGui.QApplication.translate("EditarImagen", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.Aceptar.setText(QtGui.QApplication.translate("EditarImagen", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

