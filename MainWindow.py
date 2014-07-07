# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jul  7 17:16:46 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 589)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_tipo = QtGui.QTableView(self.centralwidget)
        self.tabla_tipo.setGeometry(QtCore.QRect(20, 20, 121, 411))
        self.tabla_tipo.setObjectName("tabla_tipo")
        self.tabla_animal = QtGui.QTableView(self.centralwidget)
        self.tabla_animal.setGeometry(QtCore.QRect(160, 20, 241, 411))
        self.tabla_animal.setObjectName("tabla_animal")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 450, 391, 65))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_descripcion_tipo = QtGui.QLabel(self.widget)
        self.label_descripcion_tipo.setObjectName("label_descripcion_tipo")
        self.gridLayout.addWidget(self.label_descripcion_tipo, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_nombre_cientifico = QtGui.QLabel(self.widget)
        self.label_nombre_cientifico.setObjectName("label_nombre_cientifico")
        self.gridLayout.addWidget(self.label_nombre_cientifico, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_datos = QtGui.QLabel(self.widget)
        self.label_datos.setObjectName("label_datos")
        self.gridLayout.addWidget(self.label_datos, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Descripcion del tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_descripcion_tipo.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nombre Científico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nombre_cientifico.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_datos.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

