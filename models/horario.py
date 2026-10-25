class Horario:
    """Describe cuándo y dónde se desarrolla un grupo académico."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__salon = salon

    def get_dia(self):
        return self.__dia

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_fin(self):
        return self.__hora_fin

    def get_salon(self):
        return self.__salon

    def set_dia(self, dia):
        self.__dia = dia

    def set_hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def set_hora_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    def set_salon(self, salon):
        self.__salon = salon

    def mostrar_horario(self):
        print(f"Horario: {self.__dia} de {self.__hora_inicio} a {self.__hora_fin} "
              f"en {self.__salon}")