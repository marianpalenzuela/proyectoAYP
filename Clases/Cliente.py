class Cliente:

    """
    Clase Cliente
    """

    def __init__(self, nombre, cedula, edad, partido, tipo_entrada) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.partido = partido
        self.tipo_entrada = tipo_entrada

    