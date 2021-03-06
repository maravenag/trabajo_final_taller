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
import random


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
        """Se conectan los botones y la señales de la interfaz"""
        self.ui.tabla_tipo.clicked.connect(self.tabla_tipo_clicked)
        self.ui.tabla_animal.clicked.connect(self.tabla_animal_clicked)
        self.ui.btn_editar_tipo.clicked.connect(self.editar_tipo_clicked)
        self.ui.btn_agregar_animal.clicked.connect(self.agregar_animal_clicked)
        self.ui.btn_editar_animal.clicked.connect(self.editar_animal_clicked)
        self.ui.eliminar_animal.clicked.connect(self.eliminar_animal_clicked)

###Esta funcion debería ser llamada desde el controlador###
    def load_data_tipo(self):
        """Funcion que carga todos los tipos de animales dentro de una grilla,
        a través del controlador se recibe la información con la cual
        posteriormente se llena la información de la grilla
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
        """Borra todo lo del widget donde se muestran las imágenes,
        se limpian los labels donde se despliega información del animal
        , y luego se despliega la info del tipo de animal"""
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
        """Cuando se presiona la tabla animal, se presiona un animal,
        el a través del nombre del animal, se llama el controlador, el
        cual retorna el Animal() y se cargan en los respectivos labels
        los datos correspondientes, los cuales son sacados de los atributos
        del respectivo objeto"""

        index = self.ui.tabla_animal.currentIndex()
        nombre = index.data()  # nombre del animal
        animal = controller.carga_animal(nombre)
        self.ui.label_nombre_cientifico.setText(animal.nombre_cientifico)
        self.ui.label_datos.setText(animal.datos)
        self.despliega_imagenes(animal.id_animal)

    def editar_tipo_clicked(self):
        """Al presionar el boton editar se llama al formulario para poder
        hacer esta acción, para esto primero se verifica que se haya presionado
        un animal de la grilla"""
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
        """Llama al formulario el cual permite agregar un animal"""
        self.formulario = Formulario(callback=self.tabla_tipo_clicked)

    def editar_animal_clicked(self):
        """Llama al mismo formulario que el anterior, pero se pasan diferentes
        parámetros, la que este permite editar la información del animal.-"""
        index = self.ui.tabla_animal.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un animal")
            return False
        else:
            animal = index.data()
            self.formulario = Formulario(editar=1, nom_animal=animal,
                callback=self.tabla_tipo_clicked)

    def eliminar_animal_clicked(self):
        """Se verifica que se haya seleccionado un animal de la grilla, luego
        se pregunta si de verdad se desea eliminar este animal, luego se llama
        al controlador el cual elimina el animal de la base de datos.-"""
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
                animal = model.index(
                    index.row(), 0, QtCore.QModelIndex()).data()
                controller.elimina_animal(animal)
                self.tabla_tipo_clicked()

    def despliega_imagenes(self, id_animal):
        """Se reciben todas las una lista de objetos del tipo Imagen,
        se crea una grid layout, donde se despliegan las imágenes, por cada
        imagen se agrega un boton el cual es conectado a las funciones
        crea_funcion_eliminar y crea_funcion_editar, que crear una funcion
        por cada boton creado con lo cual luego se puede editar o eliminar las
        imagenes, se carga una imagen vacia con el botón agregar, donde
        el usuario posteriormente puede agregar la imagen que el desee"""
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
                    ubicacion = (imagenes[k].__dict__["ubicacion"].decode(
                        'utf-8'))
                    id_imagen = (imagenes[k].__dict__["id_imagen"])
                    widget[(i, j)] = QtGui.QWidget()
                    layoutsV[(i, j)] = QtGui.QVBoxLayout()
                    layoutsH[(i, j)] = QtGui.QHBoxLayout()
                    btns_el[(i, j)] = QtGui.QPushButton("Eliminar")
                    self.funcion_boton_eliminar = self.crea_funcion_eliminar(
                        id_imagen, ubicacion, id_animal)
                    btns_el[(i, j)].clicked.connect(
                        self.funcion_boton_eliminar)
                    btns_ed[(i, j)] = QtGui.QPushButton("Editar")
                    self.funcion_boton_editar = self.crea_funcion_editar(
                        id_imagen, ubicacion)
                    btns_ed[(i, j)].clicked.connect(
                        self.funcion_boton_editar)
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

        if (cant_imagenes / 3 == filas):
            btn_agregar = QtGui.QPushButton("Agregar")
            btn_agregar.clicked.connect(self.boton_agregar_imagen)
            layoutsV[(filas + 1, 1)] = QtGui.QVBoxLayout()
            widget[(filas + 1, 1)] = QtGui.QWidget()
            labels[(filas + 1, 1)] = QtGui.QLabel()
            self.myPixmap = QtGui.QPixmap("imagenes/sin_imagen.jpg")
            self.myScaledPixmap = self.myPixmap.scaled(200, 200,
                QtCore.Qt.KeepAspectRatio)
            labels[(filas + 1, 1)].setPixmap(self.myScaledPixmap)
            layoutsV[(filas + 1, 1)].addWidget(labels[(filas + 1, 1)])
            layoutsV[(filas + 1, 1)].addWidget(btn_agregar)
            widget[(filas + 1, 1)].setLayout(layoutsV[(filas + 1, 1)])
            self.layout.addWidget(widget[(filas + 1, 1)], filas + 1, 1)

        self.ui.scrollAreaWidgetContents.setLayout(self.layout)
        self.ui.scrollAreaWidgetContents.show()

    def borralayout(self, aLayout):
        """Elimina todo el layout y elementos del widget donde se
        almacenan las imágenes y los botones de cada imágen"""
        while aLayout.count():
            item = aLayout.takeAt(0)
            item.widget().deleteLater()

    def crea_funcion_eliminar(self, id_imagen, ubicacion, id_animal):
        """Crea una funcion para cada imagen que se agrega al widget
        donde se despliegan la imagen, esta función permite eliminar la
        fotografía"""
        def funcion_boton():
            mensaje = u"¿Desea eliminar la imagen seleccionada?"
            self.pregunta = QtGui.QMessageBox.question(self, self.tr("Eliminar"), mensaje
                 , QtGui.QMessageBox.StandardButton.Yes | QtGui.QMessageBox.StandardButton.No)
            if self.pregunta == QtGui.QMessageBox.Yes:
                controller.elimina_foto(id_imagen, ubicacion)
                self.despliega_imagenes(id_animal)
        return funcion_boton

    def crea_funcion_editar(self, id_imagen, ubicacion):
        """Crea una funcion para cada imagen que se agrega al widget
        donde se despliegan la imagen, esta función permite editar la
        fotografía"""
        def funcion_boton():
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                 "Elige la imagen", os.getcwd())
            directorio = fileName[0]

            num = random.randrange(1, 20)
            num_str = str(num)

            nombre_foto = "{0}_{1}".format(
                num_str, QtCore.QFileInfo(directorio).fileName())

            ubicacion_nueva_foto = "imagenes/{0}".format(nombre_foto)
            shutil.copy2(directorio, ubicacion_nueva_foto)

            controller.actualiza_foto(id_imagen, ubicacion_nueva_foto,
                callback=self.tabla_animal_clicked)

        return funcion_boton

    def boton_agregar_imagen(self):
        """Permite al usuario elegir la fotografia desde su computador,
        se verifica que se haya presionado algún animal, se abre la fotografía,
        se obtienen la diferente información necesaria de esta, y luego se llama
        al controlador con el cual agrega la fotografia al animal correspondiente
        en la base de datos, además en esta funcion se copia la fotografía a la
        carpeta /imagenes """
        index = self.ui.tabla_animal.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un animal")
            return False
        else:
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                 "Elige la imagen", os.getcwd(), "*.jpg *.jpeg *.png *.gif")
            directorio = fileName[0]

            num = random.randrange(1, 20)
            num_str = str(num)

            nombre_foto = "{0}_{1}".format(
                num_str, QtCore.QFileInfo(directorio).fileName())
            shutil.copy2(directorio, "imagenes/{0}".format(nombre_foto))

            index = self.ui.tabla_animal.currentIndex()
            animal = controller.carga_animal(index.data())
            controller.agregar_foto(animal.id_animal, nombre_foto,
                callback=self.tabla_animal_clicked)


def run():

    app = QtGui.QApplication(sys.argv)
    #main = MainWindow()  # lint:ok
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()