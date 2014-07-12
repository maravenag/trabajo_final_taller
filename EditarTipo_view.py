#!/usr/bin/python
# -*- coding: utf-8 -*-
from EditarTipo import Ui_Dialog
from PySide import QtGui
import controller


class EditarTipo(QtGui.QDialog):

    id_tipo = None

    def __init__(self, parent=None, id_tipo=None, callback=None):

        QtGui.QDialog.__init__(self, parent)
        self.callback = callback
        self.id_tipo = id_tipo
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.cargar_info(id_tipo)
        self.signals()
        self.show()

    def signals(self):
        """Se conectan los botones"""
        self.ui.btn_aceptar.clicked.connect(self.aceptar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def cargar_info(self, id_tipo):
        """Llama al controlador, el cual envia la info del tipo de animal
        la cual es colocada dentro de los respectivos cuadros de texto"""
        info = controller.carga_info_tipo(id_tipo)
        self.ui.line_edit_tipo.setText(info.nombre)
        #self.ui.line_edit_descripcion.setText(info.descripcion)
        self.ui.text_edit_descripcion.setPlainText(info.descripcion)

    def aceptar(self):
        """Al aceptar se recibe la info de la vista, se llama al controlador
        el cual envia la info a través de la función actualiza_tipo, la cual
        es luego procesada en el model"""
        nombre = self.ui.line_edit_tipo.text()
        descripcion = self.ui.text_edit_descripcion.toPlainText()
        controller.actualiza_tipo(nombre, descripcion, self.id_tipo)
        self.callback()
        self.close()

    def cancelar(self):
        """Se cierra la ventana"""
        self.close()