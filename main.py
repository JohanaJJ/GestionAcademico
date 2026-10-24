from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

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

# FASE 3: herencia (Estudiante, Docente y Administrativo)

estudiante = Estudiante("1000000002", "Lucia Rangel", "Luciarge@gmail.com",
                        "E001", matematicas, 4, 4.2)
docente = Docente("30000001", "Natalia Torres", "natalia.torres@gmail.com",
                  "D001", "Ciencias", "Tiempo completo", 40)
administrativo = Administrativo("40000001", "David Herrera", "davidher@gmail.com",
                                "A001", "Registro Académico", "Coordinadora", "Diurna")

print("\nFASE 3: DATOS COMUNES HEREDADOS DE PERSONA")
estudiante.mostrar_informacion()
print()
docente.mostrar_informacion()
print()
administrativo.mostrar_informacion()

print("\n FASE 3: DATOS PROPIOS DE CADA TIPO")
print("Estudiante:", estudiante.get_codigo_estudiantil(),
      "|", estudiante.get_programa().get_nombre(),
      "| Semestre", estudiante.get_semestre(),
      "| Promedio", estudiante.get_promedio())
print("Docente:", docente.get_numero_empleado(),
      "|", docente.get_facultad(),
      "|", docente.get_tipo_contratacion(),
      "|", docente.get_horas_semanales(), "horas")
print("Administrativo:", administrativo.get_numero_empleado(),
      "|", administrativo.get_dependencia(),
      "|", administrativo.get_cargo(),
      "|", administrativo.get_jornada())

print("\nFASE 3: ¿SON PERSONAS?")
print("El estudiante es una Persona:", isinstance(estudiante, Persona))
print("El docente es una Persona:", isinstance(docente, Persona))
print("El administrativo es una Persona:", isinstance(administrativo, Persona))

print("\nFASE 3: VALIDACIÓN EN LAS SUBCLASES")
estudiante.set_promedio(7)
docente.set_horas_semanales(-5)
estudiante.set_correo("") 

# FASE 4: comportamientos particulares (sobrescritura)

print("\n=== FASE 4: ACTIVIDAD PRINCIPAL DE CADA TIPO ===")
estudiante.realizar_actividad_principal()
docente.realizar_actividad_principal()
administrativo.realizar_actividad_principal()


# FASE 5: polimorfismo (una sola colección y un único ciclo)

estudiante2 = Estudiante("1000000003", "Camilo Pérez", "camilo.perez@gmail.com",
                         "E002", medicina, 2, 3.8)
docente2 = Docente("30000002", "Andrés Londoño", "andres.londono@gmail.com",
                   "D002", "Ciencias de la Salud", "Cátedra", 12)
administrativo2 = Administrativo("40000002", "Sofía Gómez", "sofia.gomez@gmail.com",
                                 "A002", "Tecnología", "Analista de soporte", "Mixta")

comunidad = [estudiante, docente, administrativo,
             estudiante2, docente2, administrativo2]

print("\n=== FASE 5: REPORTE GENERAL (POLIMORFISMO) ===")
for persona in comunidad:
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()
    print("-" * 50)