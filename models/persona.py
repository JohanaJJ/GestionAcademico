from abc import ABC, abstractmethod


class Persona(ABC):
    """Clase abstracta: representa lo común a toda persona de la comunidad académica:
    identificación, nombre y correo."""

    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def set_nombre(self, nombre):
        if nombre.strip() == "":
            print("Aviso: el nombre ingresado está vacío, no se modificó.")
            return False
        self.__nombre = nombre
        return True

    def set_correo(self, correo):
        if correo.strip() == "":
            print("Aviso: el correo ingresado está vacío, no se modificó.")
            return False
        self.__correo = correo
        return True

    def mostrar_informacion(self):
        print(f"Identificación: {self.__identificacion}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    @abstractmethod
    def realizar_actividad_principal(self):
        """Cada clase derivada debe definir su propia actividad."""
        pass