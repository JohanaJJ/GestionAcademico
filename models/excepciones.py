class SistemaAcademicoError(Exception):
    pass


class EstudianteYaMatriculadoError(SistemaAcademicoError):
    def __init__(self, nombre, codigo_grupo):
        super().__init__(f"{nombre} ya está en el grupo {codigo_grupo}.")


class GrupoLlenoError(SistemaAcademicoError):
    def __init__(self, codigo_grupo, capacidad):
        super().__init__(f"El grupo {codigo_grupo} no tiene cupos (máximo {capacidad}).")


class EstudianteNoMatriculadoError(SistemaAcademicoError):
    def __init__(self, codigo_estudiante, codigo_grupo):
        super().__init__(f"El estudiante {codigo_estudiante} no está en el grupo {codigo_grupo}.")


class AsignaturaNoEncontradaError(SistemaAcademicoError):
    def __init__(self, codigo):
        super().__init__(f"No se encontró la asignatura {codigo}.")


class ProgramaNoEncontradoError(SistemaAcademicoError):
    def __init__(self, codigo):
        super().__init__(f"No se encontró el programa {codigo}.")