from Funciones.Util import *
from Clases.Entrada import Entrada


"""Modulo 2: Gestion de venta de entradas"""
class Modulo2:

    def __init__(self, equipos, estadios, partidos, facturas) -> None:
        self.equipos = equipos
        self.estadios = estadios
        self.partidos = partidos
        self.facturas = facturas

    

    def menu(self):
        run = True
        while(run):
            limpiar()
            print(f"""
            1. Comprar entrada
            2. Regresar al menu principal
             """)
            
            opcion = input_opciones(2)

            if opcion == 1:
                self.opcion1()
            
            elif opcion == 2:
                run = False

    

    def opcion1(self):
        limpiar()
        nombre = input_str("Ingrese nombre: ")
        cedula = input_int("Ingrese cedula: ")
        edad = input_int("Ingrese edad: ")

        limpiar()
        for idx, partido in enumerate(self.partidos):
            equipo1_ID = partido.casa
            equipo2_ID = partido.fuera_casa

            for equipo in self.equipos:

                if equipo.id == equipo1_ID:
                    equipo1 = equipo
                
                elif equipo.id == equipo2_ID:
                    equipo2 = equipo
            
            print(f"{idx+1}. {equipo1.nombre} vs {equipo2.nombre}")
        
        opcion = input_opciones(len(self.partidos))
        partido_seleccionado = self.partidos[opcion-1]
        
        limpiar()     
        print("1.General\n2.VIP")
        tipo_entrada = input_opciones(2)

        if tipo_entrada == 1:            
            asientos = partido_seleccionado.asientos_general
        
        if tipo_entrada == 2:            
            asientos = partido_seleccionado.asientos_vip
        
        limpiar()
        for x in asientos:
            print(x)

        fila = input_int("Ingresa el numero de fila del asiento: ")
        columna = input_int("Ingresa el numero de columna del asiento: ")

        if asientos[fila-1][columna-1] == ["x"]:
            print("Asiento ya ocupado")
            salir()

        else:
            asientos[fila-1][columna-1] = ["x"]

            limpiar()           
            for x in asientos:
                print(x)

            #Imprimir costo de la entrada
            if tipo_entrada == 1:
                tipo_str = "general"
                precio = 35
            elif tipo_entrada == 2:
                tipo_str = "vip"
                precio = 75
            
            IVA = (precio*16)/100
            descuento = 0
            if es_vampiro(cedula):
                descuento = (precio*50)/100

            total = precio + IVA - descuento

            print(f"""
            -----------------------------
            Costo de la entrada
            Entrada {tipo_str}: {precio}$
            IVA: {IVA}$
            Descuento: {descuento}$
            ------------------------------
            Total: {total}$

            Desea confirmar la compra de la entrada?
            1.Si
            2.No""")

            entrada = Entrada(
                nombre,
                cedula,
                edad,
                tipo_entrada, 
                total,
                fila, 
                columna
            )

            confirmar = input_opciones(2)
            if confirmar == 1:
                limpiar()
                partido_seleccionado.entradas.append(entrada)
                print("pago realizado con exito!")
                entrada.mostrarInfo()
                salir()
            else:
                salir()


