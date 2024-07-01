class Partido:

    """Constructor"""

    def __init__(self, id, numero, casa, fuera_casa, fecha, grupo, id_estadio, asientos_general, asientos_vip) -> None:
        self.id = id
        self.numero = numero
        self.casa = casa
        self.fuera_casa = fuera_casa
        self.fecha = fecha
        self.grupo = grupo
        self.id_estadio = id_estadio
        self.asientos_general = asientos_general
        self.asientos_vip = asientos_vip
        self.entradas = []


    """Metodo para enseñar la informacion de la clase"""
    
    def mostrarInfo(self):
        print(f"""
        ID: {self.id}
        Numero: {self.numero}
        Casa: {self.casa}
        Fuera de casa: {self.fuera_casa}
        Fecha: {self.fecha}
        Grupo: {self.grupo}
        ID estadio: {self.id_estadio}
        Boletos vendidos: {len(self.entradas)}
        """)

    