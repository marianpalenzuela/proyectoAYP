from Funciones.Util import *


"""Modulo 6: Indicadores de gestion (Estadisticas)"""
class Modulo6:

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
            1. Promedio de gasto de un cliente
            2. Partidos con mejor asistencia
            3. Partido con mas boletos vendidos
            4. Top 3 productos mas vendidos de un restaurante
            5. Top 3 clientes que mas compraron boletos
            6. Regresar al menu principal
            """)

            opcion = input_opciones(6)

            if opcion == 1:
                self.opcion1()

            elif opcion == 2:
                self.opcion2()

            elif opcion == 3:
                self.opcion3()

            elif opcion == 4:
                self.opcion4()

            elif opcion == 5:
                self.opcion5()

            elif opcion == 6:
                run = False
    

    def opcion1(self):
        limpiar()
        cedula = input_int("Ingrese cedula: ")

        gastos = []

        for factura in self.facturas:
            if factura.cedula == cedula:
                gastos.append(factura.total)
        
        for partido in self.partidos:

            for entrada in partido.entradas:
                if entrada.cedula == cedula:
                    gastos.append(entrada.total)

        promedio = sum(gastos)/len(gastos)
        print(f"El promedio es de {promedio}")

        salir()

    def opcion2(self):
        limpiar()
        num_asistencias = []
        partidos = self.partidos[:]

        for partido in self.partidos:

            asistencias = 0
            for entrada in partido.entradas:

                if entrada.asistencia:
                    asistencias += 1
        
            num_asistencias.append(asistencias)
        
        count = 1
        while len(num_asistencias) != 0:
            asistencia_max = max(num_asistencias)
            idx = num_asistencias.index(asistencia_max)

            print(f"{count}.")
            partidos[idx].mostrarInfo()

            num_asistencias.pop(idx)
            partidos.pop(idx)

            count += 1

        salir()

    
    def opcion3(self):
        limpiar()
        num_boletos = []
        partidos = self.partidos[:]

        for partido in self.partidos:
            num_boletos.append(len(partido.entradas))

            
        
        count = 1
        while len(num_boletos) != 0:
            asistencia_max = max(num_boletos)
            idx = num_boletos.index(asistencia_max)

            print(f"{count}.")
            partidos[idx].mostrarInfo()

            num_boletos.pop(idx)
            partidos.pop(idx)

            count += 1

        salir()
    

    def opcion4(self):
        limpiar()
        nombre_restaurante = input_str("Ingrese nombre del restaurante: ")
        
        ventas_totales = {}

        for factura in self.facturas:
            if factura.restaurante == nombre_restaurante:
                if factura.producto in ventas_totales:
                    ventas_totales[factura.producto] += factura.cantidad
                else:
                    ventas_totales[factura.producto] = factura.cantidad
        
        productos_ordenados = sorted(ventas_totales.items(), key=lambda item: item[1], reverse=True)

        top_3_productos = productos_ordenados[:3]

        if len(top_3_productos) == 0:
            print("No se han vendido productos en el restaurante")

        else:
            print("Top 3 productos más vendidos:")
            for producto, cantidad in top_3_productos:
                print(f"{producto}: {cantidad} unidades")
        
        salir()
    

    def opcion5(self):
        limpiar()
        ventas_totales = {}

        for partido in self.partidos:            
            
            for entrada in partido.entradas:

                if entrada.nombre in ventas_totales:
                    ventas_totales[entrada.nombre] += 1
                else:
                    ventas_totales[entrada.nombre] = 1
        
        ventas_ordenadas = sorted(ventas_totales.items(), key=lambda item: item[1], reverse=True)

        top_3_productos = ventas_ordenadas[:3]

        if len(top_3_productos) == 0:
            print("No se han vendido productos en el restaurante")
            
        else:
            print("Top 3 Clientes que mas boletos compraron:")
            for cliente, cantidad in top_3_productos:
                print(f"{cliente}: {cantidad} unidades")
        
        salir()


            