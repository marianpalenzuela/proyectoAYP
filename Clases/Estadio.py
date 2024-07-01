class Estadio:

    """Constructor"""

    def __init__(self, id, nombre, ciudad, capacidad) -> None:
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.restaurantes = []

    """Metodo para enseñar la informacion de la clase"""

    def mostrarInfo(self):
        print(f"""
        ID: {self.id}
        Nombre: {self.nombre}
        Ciudad: {self.ciudad}
        Capacidad: {self.capacidad}
        Restaurantes: {self.restaurantes} #Cambiar
        """)
    