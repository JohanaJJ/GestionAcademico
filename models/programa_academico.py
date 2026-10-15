class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, num_semestres):
        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad
        self.num_semestres = num_semestres

    def mostrar_informacion(self):
        print(f"Programa [{self.codigo}]: {self.nombre}")
        print(f"Facultad: {self.facultad}")
        print(f"Número de semestres: {self.num_semestres}")