#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys
import controller
from PySide import QtGui, QtCore
from MainWindow import Ui_MainWindow
from EditarTipo_view import EditarTipo
from Formulario_view import Formulario
import os
import shutil

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.layout = QtGui.QGridLayout()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data_tipo()
        self.signals()
        self.show()

    def signals(self):
        self.ui.tabla_tipo.clicked.connect(self.tabla_tipo_clicked)
        self.ui.tabla_animal.clicked.connect(self.tabla_animal_clicked)
        self.ui.btn_editar_tipo.clicked.connect(self.editar_tipo_clicked)
        self.ui.btn_agregar_animal.clicked.connect(self.agregar_animal_clicked)
        self.ui.btn_editar_animal.clicked.connect(self.editar_animal_clicked)
        self.ui.eliminar_animal.clicked.connect(self.eliminar_animal_clicked)

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
        self.ui.tabla_tipo.setColumnWidth(0, 187)

    def tabla_tipo_clicked(self):
        self.borralayout(self.layout)
        index = self.ui.tabla_tipo.currentIndex()
        id_tipo = index.row() + 1
        tipo = controller.carga_info_tipo(id_tipo)
        self.ui.label_datos.setText("")
        self.ui.label_nombre_cientifico.setText("")
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

        self.ui.lbl_cant_ani.setText(str(r))
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
        self.despliega_imagenes(animal.id_animal)  # Acá debo pasar la id_animal

    def editar_tipo_clicked(self):
        index_ed = self.ui.tabla_tipo.currentIndex()
        if index_ed.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un tipo")
            return False
        else:
            id_tipo = index_ed.row() + 1
            self.edit = EditarTipo(id_tipo=id_tipo,
                 callback=self.load_data_tipo)

    def agregar_animal_clicked(self):
        self.formulario = Formulario()

    def editar_animal_clicked(self):
        index = self.ui.tabla_animal.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un animal")
            return False
        else:
            animal = index.data()
            self.formulario = Formulario(editar=1, nom_animal=animal)

    def eliminar_animal_clicked(self):
        model = self.ui.tabla_animal.model()
        index = self.ui.tabla_animal.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un animal")
            return False
        else:
            mensaje = u"¿Desea eliminar el animal seleccionado?"
            self.pregunta = QtGui.QMessageBox.question(self, self.tr("Eliminar"), mensaje
                 , QtGui.QMessageBox.StandardButton.Yes | QtGui.QMessageBox.StandardButton.No)
            if self.pregunta == QtGui.QMessageBox.Yes:
                animal = model.index(index.row(), 0, QtCore.QModelIndex()).data()
                controller.elimina_animal(animal)
                self.tabla_tipo_clicked()

    def despliega_imagenes(self, id_animal):
        self.borralayout(self.layout)
        imagenes = controller.obtener_imagenes(id_animal)
        cant_imagenes = len(imagenes)
        labels = {}
        widget = {}
        layoutsV = {}
        layoutsH = {}
        btns_el = {}
        btns_ed = {}
        filas = math.ceil(cant_imagenes / 3.0)
        k = 0
        cont = 0
        for i in range(int(filas)):
            for j in range(3):
                cont = cont + 1
                if(k <= cant_imagenes - 1):
                    ubicacion = (imagenes[k].__dict__["ubicacion"].decode('utf-8'))
                    id_imagen = (imagenes[k].__dict__["id_imagen"])
                    widget[(i, j)] = QtGui.QWidget()
                    layoutsV[(i, j)] = QtGui.QVBoxLayout()
                    layoutsH[(i, j)] = QtGui.QHBoxLayout()
                    btns_el[(i, j)] = QtGui.QPushButton("Eliminar")
                    self.funcion_boton_eliminar = self.crea_funcion_eliminar(id_imagen, ubicacion) # Crea un funcion para el boton creado
                    btns_el[(i, j)].clicked.connect(self.funcion_boton_eliminar) # Conecto el boton creado con la funcion
                    btns_ed[(i, j)] = QtGui.QPushButton("Editar")
                    self.funcion_boton_editar = self.crea_funcion_editar(id_imagen) # Crea un funcion para el boton creado
                    btns_ed[(i, j)].clicked.connect(self.funcion_boton_editar) # Conecto el boton creado con la funcion
                    labels[(i, j)] = QtGui.QLabel(ubicacion)
                    self.myPixmap = QtGui.QPixmap(ubicacion)
                    self.myScaledPixmap = self.myPixmap.scaled(200, 200,
                            QtCore.Qt.KeepAspectRatio)
                    labels[(i, j)].setPixmap(self.myScaledPixmap)
                    layoutsV[(i, j)].addWidget(labels[(i, j)])
                    layoutsH[(i, j)].addWidget(btns_ed[(i, j)])
                    layoutsH[(i, j)].addWidget(btns_el[(i, j)])
                    layoutsV[(i, j)].addLayout(layoutsH[(i, j)])
                    widget[(i, j)].setLayout(layoutsV[(i, j)])
                    self.layout.addWidget(widget[(i, j)], i, j)
                    k = k + 1
                if(cont == cant_imagenes + 1):
                    btn_agregar = QtGui.QPushButton("Agregar")
                    btn_agregar.clicked.connect(self.boton_agregar_imagen)
                    layoutsV[(i, j)] = QtGui.QVBoxLayout()
                    widget[(i, j)] = QtGui.QWidget()
                    labels[(i, j)] = QtGui.QLabel()
                    self.myPixmap = QtGui.QPixmap("imagenes/sin_imagen.jpg")
                    self.myScaledPixmap = self.myPixmap.scaled(200, 200,
                        QtCore.Qt.KeepAspectRatio)
                    labels[(i, j)].setPixmap(self.myScaledPixmap)
                    layoutsV[(i, j)].addWidget(labels[(i, j)])
                    layoutsV[(i, j)].addWidget(btn_agregar)
                    widget[(i, j)].setLayout(layoutsV[(i, j)])
                    self.layout.addWidget(widget[(i, j)], i, j)

        self.ui.widget.setLayout(self.layout)
        self.ui.widget.show()

    def borralayout(self, aLayout):  # Elimina todo del layout
        while aLayout.count():
            item = aLayout.takeAt(0)
            item.widget().deleteLater()

    def crea_funcion_eliminar(self, id_imagen, ubicacion):
        def funcion_boton():
                controller.elimina_foto(id_imagen, ubicacion)
        return funcion_boton

    def crea_funcion_editar(self, id_imagen):
        def funcion_boton():
            print id_imagen  # Acá va la logica del update foto
        return funcion_boton

    def boton_agregar_imagen(self):
        index = self.ui.tabla_animal.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un animal")
            return False
        else:
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                 "Elige la imagen", os.getcwd())
            directorio = fileName[0]
            nombre_foto = QtCore.QFileInfo(directorio).fileName()
            shutil.copy2(directorio, "imagenes/{0}".format(nombre_foto))

            index = self.ui.tabla_animal.currentIndex()
            animal = controller.carga_animal(index.data())
            controller.agregar_foto(animal.id_animal, nombre_foto)

def run():

    app = QtGui.QApplication(sys.argv)
    main = MainWindow()  # lint:ok
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()