class Producto:

    """Constructor"""
    
    def __init__(self, nombre, cantidad, precio, stock, adicional) -> None:
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.adicional = adicional

    """Metodo para enseñar la informacion de la clase"""

    def mostrarInfo(self):
        print(f"""
        Nombre: {self.nombre}
        Cantidad: {self.cantidad}
        Precio: {self.precio}
        Stock: {self.stock}
        Adicional: {self.adicional}
        """)