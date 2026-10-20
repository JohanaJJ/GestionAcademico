class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, num_semestres):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.__num_semestres = num_semestres

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def get_num_semestres(self):
        return self.__num_semestres

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_facultad(self, facultad):
        self.__facultad = facultad

    def set_num_semestres(self, num_semestres):
        if num_semestres <= 0:
            print("Aviso: los semestres deben ser mayores que cero, no se modificó.")
            return False
        self.__num_semestres = num_semestres
        return True

    def mostrar_informacion(self):
        print(f"Programa [{self.__codigo}]: {self.__nombre}")
        print(f"Facultad: {self.__facultad}")
        print(f"Número de semestres: {self.__num_semestres}")