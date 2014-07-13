# -*- coding: utf-8 -*-
from Formulario import Ui_Formulario
import controller
from PySide import QtGui

class Formulario(QtGui.QMainWindow):

    nom_animal = ""
    editar = None

    def __init__(self, parent=None, editar=None, nom_animal="", callback=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.callback = callback
        self.editar = editar
        self.animal = nom_animal
        self.id_animal = None
        self.id_tipo = None
        self.ui = Ui_Formulario()
        self.ui.setupUi(self)
        self.combobox_tipos()
        self.ui.Cancelar.clicked.connect(self.cerrar)
        if(self.editar == 1):
            self.ui.Aceptar.clicked.connect(self.editar_datos_animal)
            self.load_info()
        else:
            self.ui.Aceptar.clicked.connect(self.ingresa_datos_animal)
            self.ui.comboBox.setCurrentIndex(-1)
        self.show()

    def combobox_tipos(self):
        """Se carga la información en el combobox y se hace la conexión cuando
        este entra en uso"""
        tipos = [{"id":"1", "nombre":"Mamifero"},
                 {"id":"2", "nombre":"Ave"},
                 {"id":"3", "nombre":"Reptil"},
                 {"id":"4", "nombre":"Anfibio"},
                 {"id":"5", "nombre":"Pez"}]
        for elemento in tipos:  # Agregar elementos al combobox
            self.ui.comboBox.addItem(elemento["nombre"], elemento["id"])
        self.ui.comboBox.activated[int].connect(self.comboActivado)

    def comboActivado(self, index):
        """Si se activa el comobobox este devuelve la id de la casilla que se
        presionó, la que coincide con el id_tipo"""
        self.id_tipo = self.ui.comboBox.itemData(index)

    def ingresa_datos_animal(self):
        """Si no se ha seleccionado un tipo de animal envia un mensaje de error,
        si se ha seleccionado un tipo, se reciben los datos y se llama al
        controlador, el cual le pasa la info al modelo y se crea el animal,
        insertandolo en la base de datos"""
        if (self.id_tipo is None):
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar un tipo")
        else:
            self.nombre_comun = self.ui.lineNombre_2.text()
            self.nombre_cientifico = self.ui.lineNombreSci.text()
            self.datos = self.ui.lineDatos.toPlainText()
            self.fk_id_tipo = self.id_tipo
            if(self.nombre_comun == ""):
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.showMessage(
                    "Debe ingresar nombre comun")
            else:
                controller.crear_animal(self.nombre_comun,
                    self.nombre_cientifico, self.datos, self.fk_id_tipo)
                self.close()
                self.callback()

    def load_info(self):
        """Si se edita el animal, se llama al controlador el cual envia
        la información del animal seleccionado, y se llena el formulario con
        la información para que posteriormente el usuario pueda modificarla"""
        animal = controller.carga_animal(self.animal)
        self.id_animal = animal.id_animal
        self.ui.lineNombreSci.setText(animal.nombre_cientifico)
        self.ui.lineNombre_2.setText(animal.nombre_comun)
        self.ui.lineDatos.setPlainText(animal.datos)
        self.ui.comboBox.setCurrentIndex(animal.fk_id_tipo - 1)
        self.id_tipo = animal.fk_id_tipo

    def editar_datos_animal(self):
        """"Recibe la información de la vista, invoca al controlador,
        luego el controlador a través del model hace la actualización de la
        información del animal"""
        self.nombre_comun = self.ui.lineNombre_2.text()
        self.nombre_cientifico = self.ui.lineNombreSci.text()
        self.datos = self.ui.lineDatos.toPlainText()
        self.fk_id_tipo = self.id_tipo
        controller.update_animal(self.id_animal, self.nombre_comun,
            self.nombre_cientifico, self.datos, self.fk_id_tipo)
        self.close()
        self.callback()

    def cerrar(self):
        self.close()

