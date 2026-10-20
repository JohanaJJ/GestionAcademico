class Asignatura:

    def __init__(self, codigo, nombre, creditos, programa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__programa = programa 

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_creditos(self):
        return self.__creditos

    def get_programa(self):
        return self.__programa

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_creditos(self, creditos):
        if creditos <= 0:
            print("Créditos inválidos: escribe un valor mayor que cero.")
            return False
        self.__creditos = creditos
        return True

    def set_programa(self, programa):
        self.__programa = programa

    def mostrar_informacion(self):
        print(f"Asignatura [{self.__codigo}]: {self.__nombre}")
        print(f"Créditos: {self.__creditos}")
        print(f"Programa: {self.__programa.get_nombre()}")