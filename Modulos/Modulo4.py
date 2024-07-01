from Funciones.Util import *


"""Modulo 4: Gestion de restaurantes"""
class Modulo4:

    def __init__(self, equipos, estadios, partidos, facturas) -> None:
        self.equipos = equipos
        self.estadios = estadios
        self.partidos = partidos
        self.facturas = facturas

    

    def menu(self):

        run = True
        while(run):
            limpiar()
            print("""
            1. Buscar por nombre
            2. Buscar por tipo
            3. Buscar por rango de precio
            4. Regresar al menu principal
            """)

            opcion = input_opciones(4)

            if opcion == 1:
                self.opcion1()
            
            elif opcion == 2:
                self.opcion2()

            elif opcion == 3:
                self.opcion3()

            elif opcion == 4:
                run = False
    

    def opcion1(self):
        limpiar()
        nombre = input_str("Ingrese nombre del producto: ")

        limpiar()
        count = 1
        for estadio in self.estadios:

            for restaurante in estadio.restaurantes:

                for producto in restaurante.productos:

                    if nombre == producto.nombre:
                        print(f"{count}. ", end=" ")
                        producto.mostrarInfo()
                        count += 1

        salir()
    

    def opcion2(self):
        limpiar()
        print("""
        1. Alcoholico
        2. No-Alcoholico
        3. Paquete
        4. Plato
        """)

        opcion = input_opciones(4)
        if opcion == 1:
            tipo = "alcoholic"
        
        elif opcion == 2:
            tipo = "non-alcoholic"
        
        elif opcion == 3:
            tipo = "package"
        
        elif opcion == 4:
            tipo = "plate"

        limpiar()
        count = 1
        for estadio in self.estadios:

            for restaurante in estadio.restaurantes:

                for producto in restaurante.productos:

                    if tipo == producto.adicional:
                        print(f"{count}. ", end=" ")
                        producto.mostrarInfo()
                        count += 1

        salir()
    


    def opcion3(self):
        limpiar()
        precio_min = input_int("Ingrese precio minimo del producto: ")
        precio_max = input_int("Ingrese precio max del producto: ")

        limpiar()
        count = 1
        for estadio in self.estadios:

            for restaurante in estadio.restaurantes:

                for producto in restaurante.productos:

                    if float(producto.precio) in range(precio_min, precio_max+1):
                        print(f"{count}. ", end=" ")
                        producto.mostrarInfo()
                        count += 1
        
        salir()