from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura

# Programas académicos
matematicas = ProgramaAcademico("MAT01", "Matemáticas", "Ciencias", 8)
medicina = ProgramaAcademico("MED01", "Medicina", "Ciencias de la Salud", 12)

# Asignaturas 
calculo = Asignatura("MA101", "Cálculo Diferencial", 4, matematicas)
algebra = Asignatura("MA102", "Álgebra Lineal", 3, matematicas)
anatomia = Asignatura("ME101", "Anatomía Humana", 5, medicina)

# Personas
persona1 = Persona("1000123097", "Ana Martínez", "ana.martinez@gmail.com")
persona2 = Persona("1048295853", "Luis Herrera", "luis.herrera@gmail.com")

print(" PROGRAMAS")
matematicas.mostrar_informacion()
print()
medicina.mostrar_informacion()

print("\nASIGNATURAS")
calculo.mostrar_informacion()
print()
algebra.mostrar_informacion()
print()
anatomia.mostrar_informacion()

print("\nPERSONAS ")
persona1.mostrar_informacion()
print()
persona2.mostrar_informacion()