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

Pendiente: la sobrescritura y el polimorfismo se explicarán al desarrollar las fases 4 y 5.

## Uso de herramientas de inteligencia artificial

Usé Claude (una herramienta de IA) para entender términos de POO, para armar la base
del código de las fases 1, 2 y 3, para preparar los diagramas en draw.io y para hacer la
conexión con GitHub. Me ayudó mucho porque los conceptos quedan más claros al ir
trabajando paso a paso. Revisé y probé el código yo misma.