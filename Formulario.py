# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulario.ui'
#
# Created: Fri Jul 11 14:38:13 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Formulario(object):
    def setupUi(self, Formulario):
        Formulario.setObjectName("Formulario")
        Formulario.resize(327, 280)
        self.layoutWidget = QtGui.QWidget(Formulario)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 304, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineNombre_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineNombre_2.setInputMask("")
        self.lineNombre_2.setText("")
        self.lineNombre_2.setObjectName("lineNombre_2")
        self.verticalLayout.addWidget(self.lineNombre_2)
        self.lineNombreSci = QtGui.QLineEdit(self.layoutWidget)
        self.lineNombreSci.setObjectName("lineNombreSci")
        self.verticalLayout.addWidget(self.lineNombreSci)
        self.lineDatos = QtGui.QLineEdit(self.layoutWidget)
        self.lineDatos.setObjectName("lineDatos")
        self.verticalLayout.addWidget(self.lineDatos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Aceptar = QtGui.QPushButton(self.layoutWidget)
        self.Aceptar.setObjectName("Aceptar")
        self.horizontalLayout.addWidget(self.Aceptar)
        self.Cancelar = QtGui.QPushButton(self.layoutWidget)
        self.Cancelar.setObjectName("Cancelar")
        self.horizontalLayout.addWidget(self.Cancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Formulario)
        QtCore.QMetaObject.connectSlotsByName(Formulario)

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QtGui.QApplication.translate("Formulario", "Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.lineNombre_2.setPlaceholderText(QtGui.QApplication.translate("Formulario", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.lineNombreSci.setPlaceholderText(QtGui.QApplication.translate("Formulario", "Nombre Científico", None, QtGui.QApplication.UnicodeUTF8))
        self.lineDatos.setPlaceholderText(QtGui.QApplication.translate("Formulario", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Formulario", "Tipo de Animal", None, QtGui.QApplication.UnicodeUTF8))
        self.Aceptar.setText(QtGui.QApplication.translate("Formulario", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancelar.setText(QtGui.QApplication.translate("Formulario", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

