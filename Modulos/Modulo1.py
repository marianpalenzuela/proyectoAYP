from Funciones.Util import *
import datetime


"""Modulo 1: Gestion de partidos y estadios"""
class Modulo1:

    def __init__(self, equipos, estadios, partidos) -> None:
        self.equipos = equipos
        self.estadios = estadios
        self.partidos = partidos


    def menu(self):
        run = True
        while(run):
            limpiar()
            print("""
            1. Buscar todos los partidos de un pais
            2. Buscar todos los partidos que se jugaran en un estadio
            3. Buscar todos los partidos que se jugaran en una fecha
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
        for idx, equipo in enumerate(self.equipos):
            print(f"{idx+1}. {equipo.nombre}")
        
        opcion = input_opciones(len(self.equipos))
        equipo_seleccionado = self.equipos[opcion-1]

        limpiar()
        count = 1
        for partido in self.partidos:
            if equipo_seleccionado.id == partido.casa or equipo_seleccionado.id == partido.fuera_casa:
                print(f"{count}.")
                partido.mostrarInfo()
                count += 1
        
        salir()


    def opcion2(self):
        limpiar()
        for idx, estadio in enumerate(self.estadios):
            print(f"{idx+1}. {estadio.nombre}")
        
        opcion = input_opciones(len(self.estadios))
        estadio_seleccionado = self.estadios[opcion-1]

        limpiar()
        count = 1
        for partido in self.partidos:
            if estadio_seleccionado.id == partido.id_estadio:
                print(f"{count}.")
                partido.mostrarInfo()
                count += 1
        
        salir()

    def opcion3(self):
        limpiar()
        dia = input_dia()
        mes = input_mes()
        año = input_año()

        fecha = datetime.date(año, mes, dia)

        count = 1
        for partido in self.partidos:

            fecha_partido = partido.fecha.split("-")
            fecha_partido = datetime.date(int(fecha_partido[0]), int(fecha_partido[1]), int(fecha_partido[2]))
            

            if fecha_partido == fecha:
                print(f"{count}.")
                partido.mostrarInfo()
                count += 1
        
        salir()



