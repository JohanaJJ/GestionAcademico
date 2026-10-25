from models.excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError


class GestorAcademico:
    """Guarda los programas y las asignaturas registrados y permite buscarlos."""

    def __init__(self):
        self.__programas = []
        self.__asignaturas = []

    def registrar_programa(self, programa):
        self.__programas.append(programa)

    def registrar_asignatura(self, asignatura):
        self.__asignaturas.append(asignatura)

    def buscar_programa(self, codigo):
        for programa in self.__programas:
            if programa.get_codigo() == codigo:
                return programa
        # Situación 5: el programa buscado no existe
        raise ProgramaNoEncontradoError(codigo)

    def buscar_asignatura(self, codigo):
        for asignatura in self.__asignaturas:
            if asignatura.get_codigo() == codigo:
                return asignatura
        # Situación 4: la asignatura buscada no existe
        raise AsignaturaNoEncontradaError(codigo)