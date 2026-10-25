# Sistema de Gestión Académica

Actividad colaborativa N°2: evolución del Sistema de Gestión Académica

## Integrantes

- Johana Jiménez

## Descripción general

Es un sistema que organiza la información básica de una universidad: personas,
programas académicos, asignaturas y grupos. Es un solo proyecto que he ido
mejorando por fases con POO en Python.

## Estructura de los archivos

- `main.py`: el programa principal, con las pruebas.
- `models/`: las clases del sistema (`persona.py`, `estudiante.py`, `docente.py`, `administrativo.py`, `programa_academico.py`, `asignatura.py`, `horario.py`, `grupo_academico.py` y `excepciones.py`).
- `controllers/gestor_academico.py`: guarda programas y asignaturas y permite buscarlos.
- `Diagramas/`: los diagramas de clases hechos en draw.io.
- `Documentos/`: el documento de decisiones de diseño.

## Cómo ejecutarlo

Con Python instalado, en la carpeta del proyecto se escribe:

```
py main.py
```

## Herencia, sobrescritura y polimorfismo

**Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`. Así
reutilizan la identificación, el nombre, el correo y sus métodos sin escribirlos otra vez.
Cada clase agrega solo lo suyo y usa `super().__init__()` para pasarle a `Persona` los
datos que tienen en común.

**Sobrescritura:** las tres clases cambian `mostrar_informacion()`, que primero llama al
de `Persona` con `super()` y después muestra sus datos propios. También cambian
`realizar_actividad_principal()`, que da un mensaje distinto según el tipo de persona.

**Polimorfismo:** en `main.py` hay una sola lista con estudiantes, docentes y
administrativos, y se recorre con un solo `for`. En cada vuelta se llaman los mismos
métodos y Python usa la versión que le toca a cada objeto, sin necesidad de preguntar de
qué tipo es.

**Clase abstracta:** `Persona` ahora es abstracta y su método `realizar_actividad_principal()`
también. Por eso no se puede crear una `Persona` directamente, solo un `Estudiante`,
un `Docente` o un `Administrativo`.

## Grupo académico y horario

`GrupoAcademico` recibe una `Asignatura` y un `Docente` que ya están creados, y crea su
propio `Horario` dentro del constructor. Usé composición porque un horario solo tiene
sentido dentro de un grupo: el grupo "tiene un" horario. No usé herencia porque un grupo
no es un tipo de horario ni al revés. La herencia se usa cuando algo "es un" tipo de otra
cosa, como un estudiante que es una persona.

## Excepciones personalizadas

Están en `models/excepciones.py`. Se lanzan donde se detecta el problema y se capturan
en `main.py`, así el programa no se detiene:

- Estudiante ya matriculado
- Grupo lleno
- Retiro de un estudiante que no está matriculado
- Asignatura que no existe
- Programa que no existe

## Uso de herramientas de inteligencia artificial

Usé Claude (una herramienta de IA) para entender los temas de POO, para armar la base
del código de las dos actividades, para preparar los diagramas en draw.io, para conectar
el proyecto con GitHub y para organizar el documento de decisiones. Me sirvió porque fui
entendiendo los conceptos paso a paso. Después revisé el código, lo probé y cambié los
mensajes y los datos para dejarlos a mi manera.

## Versiones

- Actividad Colaborativa 1: etiqueta `Entrega_AC1`
- Actividad Colaborativa 2: etiqueta `Entrega_AC2`