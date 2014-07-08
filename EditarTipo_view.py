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
        self.ui.btn_aceptar.clicked.connect(self.aceptar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def cargar_info(self, id_tipo):
        info = controller.carga_info_tipo(id_tipo)
        self.ui.line_edit_tipo.setText(info.nombre)
        self.ui.line_edit_descripcion.setText(info.descripcion)

    def aceptar(self):
        nombre = self.ui.line_edit_tipo.text()
        descripcion = self.ui.line_edit_descripcion.text()
        controller.actualiza_tipo(nombre, descripcion, self.id_tipo)
        self.callback()
        self.close()

    def cancelar(self):
        self.close()