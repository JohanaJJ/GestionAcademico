from models.horario import Horario
from models.excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
)


class GrupoAcademico:
    """Grupo en el que se ofrece una asignatura."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_fin, salon):
        self.__codigo = codigo
        self.__asignatura = asignatura     
        self.__docente = docente            
        self.__capacidad_maxima = capacidad_maxima
        self.__estudiantes = []          
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    # ----- Métodos de consulta (get) -----
    def get_codigo(self):
        return self.__codigo

    def get_asignatura(self):
        return self.__asignatura

    def get_docente(self):
        return self.__docente

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima

    def get_horario(self):
        return self.__horario

    def get_estudiantes(self):
        return self.__estudiantes

    # ----- Método de modificación (set) -----
    def set_capacidad_maxima(self, capacidad_maxima):
        if capacidad_maxima <= 0:
            print("No se pudo cambiar la capacidad: debe ser mayor que cero.")
            return False
        self.__capacidad_maxima = capacidad_maxima
        return True

    # ----- Comportamientos del grupo -----
    def mostrar_informacion_grupo(self):
        print(f"Grupo [{self.__codigo}]: {self.__asignatura.get_nombre()}")
        print(f"Docente responsable: {self.__docente.get_nombre()}")
        print(f"Capacidad máxima: {self.__capacidad_maxima}")
        print(f"Estudiantes matriculados: {len(self.__estudiantes)}")
        self.__horario.mostrar_horario()

    def matricular_estudiante(self, estudiante):
        # Situación 1: el estudiante ya está matriculado
        for matriculado in self.__estudiantes:
            if matriculado.get_codigo_estudiantil() == estudiante.get_codigo_estudiantil():
                raise EstudianteYaMatriculadoError(estudiante.get_nombre(), self.__codigo)
        # Situación 2: el grupo está lleno
        if len(self.__estudiantes) >= self.__capacidad_maxima:
            raise GrupoLlenoError(self.__codigo, self.__capacidad_maxima)
        self.__estudiantes.append(estudiante)
        print(f"{estudiante.get_nombre()} se matriculó en el grupo {self.__codigo}.")

    def retirar_estudiante(self, codigo_estudiantil):
        for matriculado in self.__estudiantes:
            if matriculado.get_codigo_estudiantil() == codigo_estudiantil:
                self.__estudiantes.remove(matriculado)
                print(f"{matriculado.get_nombre()} se retiró del grupo {self.__codigo}.")
                return
        # Situación 3: el estudiante no estaba matriculado
        raise EstudianteNoMatriculadoError(codigo_estudiantil, self.__codigo)

    def mostrar_estudiantes(self):
        print(f"Estudiantes del grupo {self.__codigo}:")
        if len(self.__estudiantes) == 0:
            print("  (no hay estudiantes matriculados)")
        for estudiante in self.__estudiantes:
            print(f"  - {estudiante.get_codigo_estudiantil()} | {estudiante.get_nombre()}")