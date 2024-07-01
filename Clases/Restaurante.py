class Restaurante:

    """Constructor"""

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.productos = []

    """Metodo para enseñar la informacion de la clase"""

    def mostrarInfo(self):
        print(f"""
        Nombre: {self.nombre}
        Productos: {self.productos} #Cambiar
        """)