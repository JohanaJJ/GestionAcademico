from models.persona import Persona

class Administrativo(Persona):

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__dependencia = dependencia
        self.__cargo = cargo
        self.__jornada = jornada

    def get_numero_empleado(self):
        return self.__numero_empleado

    def get_dependencia(self):
        return self.__dependencia

    def get_cargo(self):
        return self.__cargo

    def get_jornada(self):
        return self.__jornada

    def set_numero_empleado(self, numero_empleado):
        self.__numero_empleado = numero_empleado

    def set_dependencia(self, dependencia):
        self.__dependencia = dependencia

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_jornada(self, jornada):
        self.__jornada = jornada