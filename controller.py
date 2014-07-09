# -*- coding: utf-8 -*-
from model import Animal, Tipo


def carga_tipos():

    tipos = Tipo.all()
    return tipos


def carga_animales(id_tipo):

    animales = Animal.animales(id_tipo)
    return animales


def carga_info_tipo(id_tipo):

    tipo = Tipo(id_tipo)
    return tipo


def carga_animal(nombre):

    """Funcion que carga un animal por nombre y lo retorna a la vista"""
    animal = Animal(nombre_comun=nombre)
    return animal


def actualiza_tipo(nombre, descripcion, id_tipo):

    tipo = Tipo(id_tipo=id_tipo)
    tipo.nombre = nombre
    tipo.descripcion = descripcion
    tipo.update_tipo()


def crear_animal(nombre_comun, nombre_cientifico, datos, fk_id_tipo):

    animal = Animal()
    animal.nombre_comun = nombre_comun
    animal.nombre_cientifico = nombre_cientifico
    animal.datos = datos
    animal.fk_id_tipo = fk_id_tipo
    animal.insert_animal()


def update_animal(id_animal, nombre_comun, nombre_cientifico,
     datos, fk_id_tipo):

    animal = Animal(id_animal=id_animal)
    animal.nombre_comun = nombre_comun
    animal.nombre_cientifico = nombre_cientifico
    animal.datos = datos
    animal.fk_id_tipo = fk_id_tipo
    animal.update_animal()