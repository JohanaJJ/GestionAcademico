# Sistema de Gestión Académica

Actividad colaborativa N°1. Construcción de un Sistema de Gestión Académica
utilizando Programación Orientada a Objetos.

## Integrantes

- Johana Jiménez

## Descripción general

Sistema que organiza la información básica de la comunidad académica de una
universidad: personas, programas académicos y asignaturas. Es un único proyecto
que se desarrolla por fases aplicando Programación Orientada a Objetos en Python.

## Estructura de los archivos

- `main.py`: programa principal con las pruebas de las fases 1, 2 y 3.
- `models/`: clases del sistema (`persona.py`, `programa_academico.py`, `asignatura.py`,
  `estudiante.py`, `docente.py` y `administrativo.py`).
- `Diagramas/`: diagramas de clases de cada fase, hechos en draw.io.

## Instrucciones para ejecutar

Con Python instalado, ejecutar en la carpeta del proyecto:

```
py main.py
```

## Herencia, sobrescritura y polimorfismo

**Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`, así que
reutilizan la identificación, el nombre, el correo y sus métodos sin repetirlos. Cada clase
agrega solo sus datos propios y usa `super().__init__()` para pasarle los datos comunes
a `Persona`.

**Sobrescritura:** las tres clases redefinen `mostrar_informacion()`, que primero llama a la
de `Persona` con `super()` y luego agrega sus datos propios, y `realizar_actividad_principal()`,
que produce un mensaje distinto para cada tipo de persona.

**Polimorfismo:** en `main.py` una sola lista con dos estudiantes, dos docentes y dos
administrativos se recorre con un único ciclo `for`. En cada vuelta se llaman los mismos
métodos y Python ejecuta la versión que corresponde al tipo real del objeto, sin usar
condicionales por tipo.

## Uso de herramientas de inteligencia artificial

Usé Claude (una herramienta de IA) para entender términos de POO, para armar la base
del código de las fases 1, 2 y 3, para preparar los diagramas en draw.io y para hacer la
conexión con GitHub. Me ayudó mucho porque los conceptos quedan más claros al ir
trabajando paso a paso. Revisé y probé el código yo misma.