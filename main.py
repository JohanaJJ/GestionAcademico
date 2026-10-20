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

# FASE 2: encapsulamiento y validaciones

print("\n FASE 2: CONSULTA CON MÉTODOS GET")
print("Nombre de la persona:", persona1.get_nombre())
print("Correo de la persona:", persona1.get_correo())
print("Semestres de", matematicas.get_nombre(), ":", matematicas.get_num_semestres())
print("Créditos de", calculo.get_nombre(), ":", calculo.get_creditos())

print("\n FASE 2: MODIFICACIONES VÁLIDAS")
persona1.set_correo("anagg@hotmail.com")
matematicas.set_num_semestres(9)
calculo.set_creditos(3)
print("Nuevo correo:", persona1.get_correo())
print("Nuevos semestres:", matematicas.get_num_semestres())
print("Nuevos créditos:", calculo.get_creditos())

print("\nFASE 2: INTENTOS DE VALORES INVÁLIDOS")
persona1.set_correo("")
matematicas.set_num_semestres(0)
calculo.set_creditos(-3)
print("Los datos se conservaron:")
print("Correo:", persona1.get_correo())
print("Semestres:", matematicas.get_num_semestres())
print("Créditos:", calculo.get_creditos())