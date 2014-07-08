# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarTipo.ui'
#
# Created: Tue Jul  8 15:24:00 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 313)
        self.line_edit_descripcion = QtGui.QLineEdit(Dialog)
        self.line_edit_descripcion.setGeometry(QtCore.QRect(30, 70, 361, 161))
        self.line_edit_descripcion.setFrame(True)
        self.line_edit_descripcion.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.line_edit_descripcion.setObjectName("line_edit_descripcion")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(160, 250, 221, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_aceptar = QtGui.QPushButton(self.widget)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.horizontalLayout_2.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtGui.QPushButton(self.widget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_2.addWidget(self.btn_cancelar)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(30, 21, 361, 44))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtGui.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.line_edit_tipo = QtGui.QLineEdit(self.widget1)
        self.line_edit_tipo.setObjectName("line_edit_tipo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_tipo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Editar Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Descripción", None, QtGui.QApplication.UnicodeUTF8))

