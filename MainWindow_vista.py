#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, controller
from model import Tipo, Animal
from PySide import QtGui, QtCore
from MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data_tipo()
        self.signals()
        self.show()

    def signals(self):
        self.ui.tabla_tipo.clicked.connect(self.tabla_tipo_clicked)
        self.ui.tabla_animal.clicked.connect(self.tabla_animal_clicked)

###Esta funcion debería ser llamada desde el controlador###
    def load_data_tipo(self):
        """Funcion que carga todos los tipos de animales dentro de una grilla
        """
        tipo = controller.carga_tipos()
        self.model = QtGui.QStandardItemModel(5, 1)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Tipo"))

        r = 0
        for row in tipo:
            nombre = row.__dict__["nombre"]
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, nombre)
            r = r + 1

        self.ui.tabla_tipo.horizontalHeader().setResizeMode(
            0, self.ui.tabla_tipo.horizontalHeader().Stretch)
        self.ui.tabla_tipo.setModel(self.model)
        self.ui.tabla_tipo.setColumnWidth(0, 121)

    def tabla_tipo_clicked(self):
        index = self.ui.tabla_tipo.currentIndex()
        id_tipo = index.row() + 1
        tipo = controller.carga_info_tipo(id_tipo)
        self.ui.label_descripcion_tipo.setText(tipo.descripcion)
        self.load_data_animal(id_tipo)

###Esta funcion también debería ser llamada desde el controlador ###
    def load_data_animal(self, id_tipo):
        """Funcion que carga todos los animales de un tipo en la grilla"""

        animales = controller.carga_animales(id_tipo)
        self.model = QtGui.QStandardItemModel(animales.__len__(), 1)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Animal"))

        r = 0
        for row in animales:
            nombre = row.__dict__["nombre_comun"]
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, nombre)
            r = r + 1

        self.ui.tabla_animal.horizontalHeader().setResizeMode(
            0, self.ui.tabla_animal.horizontalHeader().Stretch)
        self.ui.tabla_animal.setModel(self.model)
        self.ui.tabla_animal.setColumnWidth(0, 241)

    def tabla_animal_clicked(self):
        index = self.ui.tabla_animal.currentIndex()
        nombre = index.data()  # nombre del animal
        animal = controller.carga_animal(nombre)
        self.ui.label_nombre_cientifico.setText(animal.nombre_cientifico)
        self.ui.label_datos.setText(animal.datos)


def run():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()