from Funciones.Util import *
from Clases.Factura import Factura

"""Modulo 5: Gestion de venta de restaurantes"""
class Modulo5:

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
            1. Comprar producto
            2. Regresar al menu principal
            """)

            opcion = input_opciones(2)

            if opcion == 1:
                self.opcion1()

            elif opcion == 2:
                run = False
        
    
    def opcion1(self):
        limpiar()
        cedula = input_int("Ingrese cedula: ")

        find = False
        entradaVIP = None
        partido = None
        for p in self.partidos:

            for entrada in p.entradas:

                if cedula == entrada.cedula and entrada.tipo == 2:
                    find = True
                    entradaVIP = entrada
                    partido = p
                    break
        
        if not find:
            limpiar()
            print(f"El cliente con la cedula {cedula} no esta registrado como cliente VIP")
            salir()

        else:
            estadio = None
            for e in self.estadios:

                if e.id == partido.id_estadio:
                    estadio = e
            
            limpiar()
            print("--------Restaurantes--------")
            for idx, r in enumerate(estadio.restaurantes):
                print(f"{idx+1}. {r.nombre}")
            
            restaurante = estadio.restaurantes[input_opciones(len(estadio.restaurantes)+1)]

            if entradaVIP.edad >= 18:
                
                limpiar()
                print("---------Productos---------")
                for idx, p in enumerate(restaurante.productos):
                    print(f"{idx+1}. {p.nombre} --> {p.precio}")

                producto = restaurante.productos[input_opciones(len(restaurante.productos)+1)]
            
            elif entradaVIP.edad < 18:

                indices = []
                limpiar()
                for idx, p in enumerate(restaurante.productos):
                    if p.adicional != "alcoholic":
                        indices.append(idx+1)
                        print(f"{idx+1}. {p.nombre} --> {p.precio}")

                print(indices)
                producto_indice = input_int("Ingrese el numero de la opcion deseada: ")
                while producto_indice not in indices:
                    producto_indice = input_int("Error: Ingrese el numero de la opcion deseada: ")

                producto = restaurante.productos[producto_indice-1]
            
            if producto.stock <= 0:
                limpiar()
                print("No hay stock del producto")
                salir()
            
            else:
                limpiar()
                cantidad = input_int("Ingrese la cantidad del producto que desea comprar: ")

                while cantidad > producto.stock:
                    limpiar()
                    print("La cantidad supera al stock del producto")
                    cantidad = input_int("Ingrese la cantidad del producto que desea comprar: ")

                factura = Factura(
                    entradaVIP,
                    restaurante.nombre,
                    producto,
                    cantidad                    
                )

                limpiar()
                factura.mostrarInfo()
                print("Desea realizar la compra?\n1.Si\n2.No")
                opcion = input_opciones(2)

                if opcion == 1:
                    
                    self.facturas.append(factura)
                    print("La compra se ha realizado con exito!")
                
                salir()



                    
                    
                    


