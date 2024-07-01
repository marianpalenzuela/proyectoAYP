from Funciones.Util import *

class Factura:

    """Constructor"""

    def __init__(self, entrada, restaurante, producto, cantidad) -> None:
        self.entrada = entrada
        self.restaurante = restaurante
        self.producto = producto
        self.cantidad = cantidad
        self.descuento = 0
        precio = float(producto.precio) * cantidad

        if es_numero_perfecto(entrada.cedula):
            self.descuento = (precio*15)/100


        self.total = precio - self.descuento


    """Metodo para enseñar la informacion de la clase"""

    def mostrarInfo(self):
        print(f"""
        Nombre: {self.entrada.nombre}
        Cedula: {self.entrada.cedula}
        Edad: {self.entrada.edad}
        Producto: {self.producto.nombre}
        Cantidad: {self.cantidad}
        Total: {self.total}$
        """)
