# -*- coding: utf-8 -*-
import sqlite3
import os

def connect():

    """Retorna una conexión con la base de datos"""
    conn = sqlite3.connect('bd_principal.db')
    conn.row_factory = sqlite3.Row
    return conn


def last_id(conn):
    """Retorna la última primary key generada en la base de datos"""
    result = conn.execute("SELECT last_insert_rowid()")
    return result.fetchone()


class Tipo(object):

    """Clase que representa a la tabla tipo"""

    __tablename__ = "tipo"
    id_tipo = None
    nombre = ""
    descripcion = ""

    def __init__(
            self,
            id_tipo=None,
            nombre="",
            descripcion=""):

        self.id_tipo = id_tipo
        self.nombre = nombre
        self.descripcion = descripcion

        # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
        if id_tipo is not None:
            self.load_tipo()
        elif nombre is not "":
            self.load_tipo(nombre=nombre)

    def load_tipo(self, nombre=None):
        """
        Carga un tipo de la base de datos por id_tipo o nombre
        """
        conn = connect()
        query = "SELECT * FROM tipo"
        if nombre is not None:
            query += " WHERE nombre = ?"
            condition = nombre
        else:
            if self.id_tipo is None:
                return
            query += " WHERE id_tipo = ?"
            condition = self.id_tipo

        result = conn.execute(
            query, [condition])
        row = result.fetchone()
        conn.close()
        if row is not None:
            self.id_tipo = row[0]
            self.nombre = row[1]
            self.descripcion = row[2]
        else:
            self.id_tipo = None
            print "El registro no existe"

    def update_tipo(self):
        query = "UPDATE {} ".format(self.__tablename__)
        query += "SET id_tipo = ?, "
        query += "nombre = ?, "
        query += "descripcion = ?"
        query += " WHERE id_tipo = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.id_tipo,
                    self.nombre,
                    self.descripcion,
                    self.id_tipo])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla cursos.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        tipo = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            for row in data:
                tipo.append(
                    Tipo(row[0], row[1], row[2]))
            return tipo

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


class Animal(Tipo):

    __tablename__ = "animal"
    id_animal = None
    nombre_comun = ""
    nombre_cientifico = ""
    datos = ""
    fk_id_tipo = None

    def __init__(self,
            id_animal=None,
            nombre_comun="",
            nombre_cientifico="",
            datos="",
            fk_id_tipo=None):

        self.id_animal = id_animal
        self.nombre_comun = nombre_comun
        self.nombre_cientifico = nombre_cientifico
        self.datos = datos
        self.fk_id_tipo = fk_id_tipo

        if id_animal is not None:
            self.id_animal = id_animal
            self.load_animal()
        elif nombre_comun is not "":
            self.load_animal(nombre=nombre_comun)

    def load_animal(self, nombre=None):
        query = "SELECT * FROM animal "
        conn = connect()
        if self.id_animal is not None:
            query += "WHERE id_animal = ?"
            condicion = self.id_animal
        else:
            if nombre is not None:
                query += "WHERE nombre_comun = ?"
                condicion = nombre

        result = conn.execute(
            query, [condicion])
        row = result.fetchone()
        conn.close()
        if row is not None:
            self.id_animal = row[0]
            self.nombre_comun = row[1]
            self.nombre_cientifico = row[2]
            self.datos = row[3]
            self.fk_id_tipo = row[4]
        else:
            self.id_animal = None
            print "El registro no existe"

    def insert_animal(self):
        query = "INSERT INTO animal "
        query += "(nombre_comun, nombre_cientifico, datos, fk_id_tipo) "
        query += "VALUES (?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(  # lint:ok
                query, [
                    self.nombre_comun,
                    self.nombre_cientifico,
                    self.datos,
                    self.fk_id_tipo])
            conn.commit()
            id_tipo = last_id(conn)
            conn.close()
            return id_tipo
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def update_animal(self):
        query = "UPDATE animal "
        query += "SET nombre_comun = ?, "
        query += "nombre_cientifico = ?, "
        query += "datos = ?, "
        query += "fk_id_tipo = ? "
        query += "WHERE id_animal = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.nombre_comun,
                    self.nombre_cientifico,
                    self.datos,
                    self.fk_id_tipo,
                    self.id_animal])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete_animal(self):
        query = "DELETE FROM animal "
        query += "WHERE id_animal = ?"
        try:
            conn = connect()
            conn.execute(query, [self.id_animal])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def animales(cls, id_tipo):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla animales.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        query += " WHERE fk_id_tipo = {}".format(id_tipo)
        animales = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            for row in data:
                animales.append(
                    Animal(row[0], row[1], row[2]))
            return animales

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None


class Imagen(Animal):

    __tablename__ = "imagen"
    id_imagen = None
    ubicacion = ""
    formato = ""
    resolucion = ""
    fk_id_animal = ""

    def __init__(self,
            id_imagen=None,
            ubicacion="",
            formato="",
            resolucion="",
            fk_id_animal=""):

        self.id_imagen = id_imagen
        self.ubicacion = ubicacion
        self.formato = formato
        self.resolucion = resolucion
        self.fk_id_animal = fk_id_animal

    def insertar_imagen(self):
        query = "INSERT INTO imagen "
        query += "(ubicacion,formato,resolucion,fk_id_animal) "
        query += "VALUES (?,?,?,?)"
        try:
            conn = connect()
            result = conn.execute(  # lint:ok
                query, [
                    self.ubicacion,
                    self.formato,
                    self.resolucion,
                    self.fk_id_animal])
            conn.commit()
            id_tipo = last_id(conn)
            conn.close()
            return id_tipo
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    @classmethod
    def imagenes(cls, fk_id_animal):
        """Funcion que devuelve las imágenes de un animal específico"""
        query = "SELECT * FROM {}".format(cls.__tablename__)
        query += " WHERE fk_id_animal = {}".format(fk_id_animal)
        imagenes = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()

            for row in data:
                imagenes.append(
                    Imagen(row[0], row[1], row[2]))
            return imagenes

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    @classmethod
    def elimina_foto(cls, id_imagen, ubicacion):
        query = "DELETE FROM imagen "
        query += "WHERE id_imagen = '{}'".format(id_imagen)
        try:
            conn = connect()
            conn.execute(query)
            conn.commit()
            conn.close()
            os.remove(ubicacion)
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

if __name__ == '__main__':

    caballo = Imagen()
    caballo.ubicacion= "imagenes/caballo_2.jpg"
    caballo.formato="JPG",
    caballo.resolucion="234x432",
    caballo.fk_id_animal= 3
    caballo.insertar_imagen()