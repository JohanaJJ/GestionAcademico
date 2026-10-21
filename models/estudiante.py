from models.persona import Persona

class Estudiante(Persona):
    def __init__(self, identificacion, nombre, correo,
                 codigo_estudiantil, programa, semestre, promedio):
    
        super().__init__(identificacion, nombre, correo)

        self.__codigo_estudiantil = codigo_estudiantil
        self.__programa = programa  # objeto de tipo ProgramaAcademico
        self.__semestre = semestre
        self.__promedio = promedio

    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def get_programa(self):
        return self.__programa

    def get_semestre(self):
        return self.__semestre

    def get_promedio(self):
        return self.__promedio

    def set_codigo_estudiantil(self, codigo_estudiantil):
        self.__codigo_estudiantil = codigo_estudiantil

    def set_programa(self, programa):
        self.__programa = programa

    def set_semestre(self, semestre):
        if semestre <= 0:
            print("No se pudo cambiar el semestre: debe ser mayor que cero.")
            return False
        self.__semestre = semestre
        return True

    def set_promedio(self, promedio):
        if promedio < 0 or promedio > 5:
            print("No se pudo cambiar el promedio: debe estar entre 0 y 5.")
            return False
        self.__promedio = promedio
        return True