class Asignatura:
    def __init__(self, codigo, nombre, creditos, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.programa = programa  # objeto de tipo ProgramaAcademico

    def mostrar_informacion(self):
        print(f"Asignatura [{self.codigo}]: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Programa: {self.programa.nombre}")