# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulario.ui'
#
# Created: Sat Jul 12 17:08:09 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Formulario(object):
    def setupUi(self, Formulario):
        Formulario.setObjectName("Formulario")
        Formulario.resize(299, 269)
        self.widget = QtGui.QWidget(Formulario)
        self.widget.setGeometry(QtCore.QRect(10, 2, 271, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineNombre_2 = QtGui.QLineEdit(self.widget)
        self.lineNombre_2.setInputMask("")
        self.lineNombre_2.setText("")
        self.lineNombre_2.setObjectName("lineNombre_2")
        self.verticalLayout.addWidget(self.lineNombre_2)
        self.lineNombreSci = QtGui.QLineEdit(self.widget)
        self.lineNombreSci.setObjectName("lineNombreSci")
        self.verticalLayout.addWidget(self.lineNombreSci)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineDatos = QtGui.QPlainTextEdit(self.widget)
        self.lineDatos.setObjectName("lineDatos")
        self.verticalLayout_2.addWidget(self.lineDatos)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Aceptar = QtGui.QPushButton(self.widget)
        self.Aceptar.setObjectName("Aceptar")
        self.horizontalLayout.addWidget(self.Aceptar)
        self.Cancelar = QtGui.QPushButton(self.widget)
        self.Cancelar.setObjectName("Cancelar")
        self.horizontalLayout.addWidget(self.Cancelar)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Formulario)
        QtCore.QMetaObject.connectSlotsByName(Formulario)

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QtGui.QApplication.translate("Formulario", "Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.lineNombre_2.setPlaceholderText(QtGui.QApplication.translate("Formulario", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.lineNombreSci.setPlaceholderText(QtGui.QApplication.translate("Formulario", "Nombre Científico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Formulario", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Formulario", "Tipo de Animal", None, QtGui.QApplication.UnicodeUTF8))
        self.Aceptar.setText(QtGui.QApplication.translate("Formulario", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancelar.setText(QtGui.QApplication.translate("Formulario", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

