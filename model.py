import sqlite3


def connect():
    """Retorna una conexión con la base de datos"""
    conn = sqlite3.connect('alumnos.db')
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
        elif nombre is not None:
            self.load_tipo(nombre=nombre)

    def load_tipo(self, nombre=None):
        """
        Carga un tipo de la base de datos por id_tipo o nombre
        """
        conn = connect()
        query = "SELECT * FROM tipo "
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

# save privado ya que se guardan distintas cosas
    def save_tipo(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
    #    if self.id_tipo is None:
   #         self.id_tipo = self.__insert()
  #      else:
        self.update_tipo()

    def update_tipo(self):
        query = "UPDATE {} ".format(self.__tablename__)
        query += "SET id_tipo = ?, "
        query += "nombre = ?, "
        query += "descripcion = ?, "
        query += "WHERE id_tipo = ?"
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

    __tablename__ = "animales"
    id_animal = None
    nombre_comun = ""
    nombre_cientifico = ""
    datos = ""
    #Revisar esta linea
    fk_id_tipo = None

    def __init__(self,
            id_animal=None,
            nombre_comun="",
            nombre_cientifico="",
            datos="",
            #Revisar esta linea y preguntar por el super
            fk_id_tipo=None):

        super(Animal, self).__init__()
        self.id_animal = id_animal
        self.nombre_comun = nombre_comun
        self.nombre_cientifico = nombre_cientifico
        self.datos = datos
        self.fk_id_tipo = fk_id_tipo

        if id_animal is not None:
            self.id_animal = id_animal
            self.load_animal()

    def load_animal(self):
        if self.id_animal is not None:
            conn = connect()
            query = "SELECT * FROM animales WHERE id_animal = ?"
            result = conn.execute(
                query, [self.id_animal])
            row = result.fetchone()
            conn.close()
            if row is not None:
                self.id_animal = row[1]
                self.nombre_comun = row[2]
                self.nombre_cientifico = row[3]
                self.datos = row[4]
                self.fk_id_tipo = row[5]
            else:
                self.id_animal = None
                print "El registro no existe"

    def insert_animal(self):
        query = "INSERT INTO animales "
        # La pk está definida como auto increment en el modelo
        query += "(id_animal, nombre_comun, nombre_cientifico, datos, fk_id_tipo) "
        query += "VALUES (?, ?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.id_tipo,
                    self.nombre_comun,
                    self.nombre_cientifico,
                    self.datos,
                    self.fk_id_tipo,
                    self.id_tipo])
            conn.commit()
            id_tipo = last_id(conn)
            conn.close()
            return id_tipo
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def update_animal(self):
        query = "UPDATE animales "
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
        query = "DELETE FROM animales "
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