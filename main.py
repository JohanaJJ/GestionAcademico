from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo
from models.grupo_academico import GrupoAcademico
from models.excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoMatriculadoError,
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError,
)
from controllers.gestor_academico import GestorAcademico

# Persona abstracta
print("=== NO SE PUEDE CREAR UNA PERSONA DIRECTAMENTE ===")
try:
    persona = Persona("1000000000", "Persona Genérica", "persona@gmail.com")
except TypeError as error:
    print("Error controlado:", error)

# Datos del sistema
gestor = GestorAcademico()

matematicas = ProgramaAcademico("MAT01", "Matemáticas", "Ciencias", 8)
medicina = ProgramaAcademico("MED01", "Medicina", "Ciencias de la Salud", 12)
gestor.registrar_programa(matematicas)
gestor.registrar_programa(medicina)

calculo = Asignatura("MA101", "Cálculo Diferencial", 4, matematicas)
algebra = Asignatura("MA102", "Álgebra Lineal", 3, matematicas)
anatomia = Asignatura("ME101", "Anatomía Humana", 5, medicina)
gestor.registrar_asignatura(calculo)
gestor.registrar_asignatura(algebra)
gestor.registrar_asignatura(anatomia)

docente1 = Docente("50943816", "Fabian Peña", "fabian.pena@gmail.com",
                   "D001", "Ciencias", "Tiempo completo", 40)
docente2 = Docente("60047765", "Daniel Londoño", "daniel.londono@gmail.com",
                   "D002", "Ciencias de la Salud", "Cátedra", 12)

estudiante1 = Estudiante("89402050", "Laura Martinez", "laura.martinez@gmail.com",
                         "E001", matematicas, 4, 4.2)
estudiante2 = Estudiante("67400593", "Ivan Pava", "ivan.pava@gmail.com",
                         "E002", matematicas, 2, 3.8)
estudiante3 = Estudiante("100754642", "Jorge Rincon", "jorge.rincon@gmail.com",
                         "E003", medicina, 1, 4.5)

administrativo1 = Administrativo("105392952", "Samanta Cruz", "samanta.cruz@gmail.com",
                                 "A001", "Registro Académico", "Coordinadora", "Diurna")
administrativo2 = Administrativo("403050394", "Jimena Valencia", "jimena.valencia@gmail.com",
                                 "A002", "Tecnología", "Analista de soporte", "Mixta")

# Grupos (cada uno crea su propio horario)
print("\n=== CREACIÓN DE GRUPOS ACADÉMICOS ===")
grupo1 = GrupoAcademico("G01", calculo, docente1, 2, "Lunes", "08:00", "10:00", "Salón 101")
grupo2 = GrupoAcademico("G02", anatomia, docente2, 3, "Miércoles", "14:00", "16:00", "Salón 205")

grupo1.mostrar_informacion_grupo()
print()
grupo2.mostrar_informacion_grupo()

# Matrículas correctas 
print("\n=== MATRÍCULA CORRECTA ===")
grupo1.matricular_estudiante(estudiante1)
grupo1.matricular_estudiante(estudiante2)
grupo2.matricular_estudiante(estudiante3)
print()
grupo1.mostrar_estudiantes()

# Excepciones
print("\n=== EXCEPCIÓN: ESTUDIANTE YA MATRICULADO ===")
try:
    grupo1.matricular_estudiante(estudiante1)
except EstudianteYaMatriculadoError as error:
    print("Error controlado:", error)

print("\n=== EXCEPCIÓN: GRUPO CON CAPACIDAD MÁXIMA ===")
try:
    grupo1.matricular_estudiante(estudiante3)   # el grupo 1 solo admite 2
except GrupoLlenoError as error:
    print("Error controlado:", error)

print("\n=== RETIRO CORRECTO ===")
try:
    grupo1.retirar_estudiante("E002")
    grupo1.mostrar_estudiantes()
except EstudianteNoMatriculadoError as error:
    print("Error controlado:", error)

print("\n=== EXCEPCIÓN: RETIRAR UN ESTUDIANTE NO MATRICULADO ===")
try:
    grupo1.retirar_estudiante("E999")
except EstudianteNoMatriculadoError as error:
    print("Error controlado:", error)

print("\n=== EXCEPCIÓN: ASIGNATURA INEXISTENTE ===")
try:
    gestor.buscar_asignatura("XX000")
except AsignaturaNoEncontradaError as error:
    print("Error controlado:", error)

print("\n=== EXCEPCIÓN: PROGRAMA INEXISTENTE ===")
try:
    gestor.buscar_programa("ZZ000")
except ProgramaNoEncontradoError as error:
    print("Error controlado:", error)

print("\nEl programa continuó su ejecución después de controlar cada excepción.")

# Polimorfismo
print("\n=== REPORTE GENERAL: POLIMORFISMO ===")
comunidad = [estudiante1, docente1, administrativo1,
             estudiante2, docente2, administrativo2, estudiante3]

for persona_vinculada in comunidad:
    persona_vinculada.mostrar_informacion()
    persona_vinculada.realizar_actividad_principal()
    print("-" * 50)