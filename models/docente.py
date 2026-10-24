from models.persona import Persona

class Docente(Persona):
    """Un docente ES una Persona: hereda identificación, nombre y correo."""

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__facultad = facultad
        self.__tipo_contratacion = tipo_contratacion
        self.__horas_semanales = horas_semanales

    # Métodos de consulta (get)
    def get_numero_empleado(self):
        return self.__numero_empleado

    def get_facultad(self):
        return self.__facultad

    def get_tipo_contratacion(self):
        return self.__tipo_contratacion

    def get_horas_semanales(self):
        return self.__horas_semanales

    # Métodos de modificación (set)
    def set_numero_empleado(self, numero_empleado):
        self.__numero_empleado = numero_empleado

    def set_facultad(self, facultad):
        self.__facultad = facultad

    def set_tipo_contratacion(self, tipo_contratacion):
        self.__tipo_contratacion = tipo_contratacion

    def set_horas_semanales(self, horas_semanales):
        if horas_semanales <= 0:
            print("No se pudo cambiar las horas semanales: deben ser mayores que cero.")
            return False
        self.__horas_semanales = horas_semanales
        return True

  
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Docente")
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Facultad: {self.__facultad}")
        print(f"Tipo de contratación: {self.__tipo_contratacion}")
        print(f"Horas semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        print(f"{self.get_nombre()} orienta clases en la Facultad de {self.__facultad}.")