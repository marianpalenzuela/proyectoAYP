from Funciones.Util import *


"""Modulo 3: Gestion de asistencia a partidos"""
class Modulo3:

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
            1. Validar entrada
            2. Regresar al menu principal
             """)
            
            opcion = input_opciones(2)

            if opcion == 1:
                self.opcion1()
            
            elif opcion == 2:
                run = False
    


    def opcion1(self):
        limpiar()
        codigo = input("Ingrese el codigo de la entrada: ")

        encontrado = False
        for partido in self.partidos:

            for entrada in partido.entradas:

                if entrada.codigo == codigo and not entrada.asistencia:
                    encontrado = True
                    entrada.asistencia = True
                    entrada.mostrarInfo()
                    print("La entrada ha sido validada!")
        
        if not encontrado:
            print("La entrada no es valida")
        
        salir()


