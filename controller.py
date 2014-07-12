# -*- coding: utf-8 -*-
from model import Animal, Tipo, Imagen
from PIL import Image
import os


def carga_tipos():
    """Devuelve una lista de objetos con todos los tipos de animales
    que se encuentran en la base de datos, como llama a una función de la clase
    para instanciarla no necesita ningun parámetro"""
    tipos = Tipo.all()
    return tipos


def carga_animales(id_tipo):
    """Devuelve una lista de objetos con todos los animales de un tipo
    que se encuentran en la base de datos, recibe como parámetro la id del tipo
    de animal del que se quiere cargar"""
    animales = Animal.animales(id_tipo)
    return animales


def carga_info_tipo(id_tipo):
    """Devuelve un objeto del tipo Tipo, como parámetro se pasa la id
    del tipo, se utiliza para posteriormente acceder a los atributos del tipo
    y cargarlos en la ventana"""
    tipo = Tipo(id_tipo)
    return tipo


def carga_animal(nombre):
    """Funcion que carga un animal por nombre y lo retorna a la vista"""
    animal = Animal(nombre_comun=nombre)
    return animal


def actualiza_tipo(nombre, descripcion, id_tipo):
    """Recibe como parámetros nombre, descripcion e id_tipo,
    carga el objeto del tipo Tipo de la base de datos, se le asignan
    los nuevos atributos y luego se hace un update de la información"""
    tipo = Tipo(id_tipo=id_tipo)
    tipo.nombre = nombre
    tipo.descripcion = descripcion
    tipo.update_tipo()


def crear_animal(nombre_comun, nombre_cientifico, datos, fk_id_tipo):
    """Crea un objeto del tipo animal, se le asignan los valores a los
    atributos de este, luego se llama a la función insert_animal()
    la cual hace el insert en la base de datos"""
    animal = Animal()
    animal.nombre_comun = nombre_comun
    animal.nombre_cientifico = nombre_cientifico
    animal.datos = datos
    animal.fk_id_tipo = fk_id_tipo
    animal.insert_animal()


def update_animal(id_animal, nombre_comun, nombre_cientifico,
     datos, fk_id_tipo):
    """Llama a un objeto del tipo animal por la id de este,
    se reasignan los valores de los atributos, luego llama a la función
    update_animal la cual hace la actualización en la base de datos"""
    animal = Animal(id_animal=id_animal)
    animal.nombre_comun = nombre_comun
    animal.nombre_cientifico = nombre_cientifico
    animal.datos = datos
    animal.fk_id_tipo = fk_id_tipo
    animal.update_animal()


def elimina_animal(nombre):
    """Recibe como parámetro el nombre del animal que se desea eliminar
    llama al objeto y luego a la función delete_animal(), la cual borra de la
    base de datos el animal"""

    animal = Animal(nombre_comun=nombre)
    animal.delete_animal()


def obtener_imagenes(id_animal):
    """Recibe como parámetro la id del animal,
    luego llama a la funcion .imagenes(), la cual devuelve una lista con
    todas las imagenes en las cuales su fk_id_animal es id_animal"""
    imagenes = Imagen.imagenes(id_animal)
    return imagenes


def elimina_foto(id_imagen, ubicacion):
    """Recibe como parámetro la id_imagen, ubicacion
    y llama a la funcion eliminar_foto que borra tanto de la base de datos
    como del disco duro"""
    Imagen.elimina_foto(id_imagen, ubicacion)


def agregar_foto(id_animal, nombre_foto, callback):
    """Recibe como parámetros la id_animal, nombre_foto y un callback,
    abre la imagen que se desea agregar, se obtienen los valores para los
    atributos , luego se crea un objeto del tipo imagen, se le pasan estos
    valores y hace el insert en la base de datos a través de la función
    insertar_imagen()"""

    ubicacion = "imagenes/{0}".format(nombre_foto)
    imagen = Image.open(ubicacion)
    tamano = "{0}x{1}".format(imagen.size[0], imagen.size[1])
    formato = imagen.format

    foto = Imagen()
    foto.ubicacion = ubicacion
    foto.formato = formato
    foto.resolucion = tamano
    foto.fk_id_animal = id_animal
    foto.insertar_imagen()
    callback()


def actualiza_foto(id_imagen, ubicacion_foto_nueva, callback):
    """Recibe como parámetros la id de la imagen y la ubicación de la foto nueva
    al igual que la función anterior se obtien la información necesaria de la
    fotografía que se quiere agregar, se crea el objeto imagen, se le pasan los
    parámetros y luego llama a la funcion update_imagen() de la clase Imagen
    la cual actualiza en la base de datos"""
    imagen_nueva = Image.open(ubicacion_foto_nueva)
    tamano = "{0}x{1}".format(imagen_nueva.size[0], imagen_nueva.size[1])
    formato = imagen_nueva.format

    imagen = Imagen(id_imagen=id_imagen)
    os.remove(imagen.ubicacion)
    imagen.ubicacion = ubicacion_foto_nueva
    imagen.formato = formato
    imagen.resolucion = tamano
    imagen.update_imagen()
    callback()