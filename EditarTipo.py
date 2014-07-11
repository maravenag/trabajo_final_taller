# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarTipo.ui'
#
# Created: Fri Jul 11 15:03:39 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 313)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 250, 221, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_aceptar = QtGui.QPushButton(self.layoutWidget)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.horizontalLayout_2.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtGui.QPushButton(self.layoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_2.addWidget(self.btn_cancelar)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 21, 361, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.line_edit_tipo = QtGui.QLineEdit(self.layoutWidget1)
        self.line_edit_tipo.setObjectName("line_edit_tipo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_edit_tipo)
        self.text_edit_descripcion = QtGui.QPlainTextEdit(Dialog)
        self.text_edit_descripcion.setGeometry(QtCore.QRect(30, 80, 361, 161))
        self.text_edit_descripcion.setObjectName("text_edit_descripcion")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Editar Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Descripción", None, QtGui.QApplication.UnicodeUTF8))

