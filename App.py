from Funciones.Util import *
from Modulos.Modulo1 import Modulo1
from Modulos.Modulo2 import Modulo2
from Modulos.Modulo3 import Modulo3
from Modulos.Modulo4 import Modulo4
from Modulos.Modulo5 import Modulo5
from Modulos.Modulo6 import Modulo6
import os


"""Clase App: Aqui se unen todos los modulos para poder construir la app"""
class App:

    def __init__(self) -> None:
        self.equipos = []
        self.estadios = []
        self.partidos = []
        self.facturas = []


    def cargarDatos(self):            
        if os.path.getsize("Datos\\equipos.txt") == 0:
            self.equipos = cargarEquipos()
            with open("Datos\\equipos.txt", 'wb') as f:
                pickle.dump(self.equipos, f)

        else:
            with open("Datos\\equipos.txt", 'rb') as f:
                self.equipos = pickle.load(f)


        if os.path.getsize("Datos\\estadios.txt") == 0:
            self.estadios = cargarEstadios()
            with open("Datos\\estadios.txt", 'wb') as f:
                pickle.dump(self.estadios, f)

        else:
            with open("Datos\\estadios.txt", 'rb') as f:
                self.estadios = pickle.load(f)
    

        if os.path.getsize("Datos\\partidos.txt") == 0:
            self.partidos = cargarPartidos(self.estadios)
            with open("Datos\\partidos.txt", 'wb') as f:
                pickle.dump(self.partidos, f)
        
        else:
            with open("Datos\\partidos.txt", 'rb') as f:
                self.partidos = pickle.load(f)

    def guardarDatos(self):
        guardar_txt("Datos\equipos.txt", self.equipos)
        guardar_txt("Datos\estadios.txt", self.estadios)
        guardar_txt("Datos\partidos.txt", self.partidos)


    def menu(self):
        self.cargarDatos()        

        run = True
        while(run):
            limpiar()
            print(f"""
                1. Gestion de partidos y estadios
                2. Gestion de venta de entradas
                3. Gestion de asistencia a partidos
                4. Gestion de restaurantes
                5. Gestion de venta de restaurantes
                6. Indicadores de gestion (Estadisticas)
                7. Guardar cambios
                8. Salir
            """)
            opcion = input_opciones(9)

            if opcion == 1:
                md = Modulo1(self.equipos, self.estadios, self.partidos)
                md.menu()
            
            elif opcion == 2:
                md = Modulo2(self.equipos, self.estadios, self.partidos, self.facturas)
                md.menu()

            elif opcion == 3:
                md = Modulo3(self.equipos, self.estadios, self.partidos, self.facturas)
                md.menu()
            
            elif opcion == 4:
                md = Modulo4(self.equipos, self.estadios, self.partidos, self.facturas)
                md.menu()

            elif opcion == 5:
                md = Modulo5(self.equipos, self.estadios, self.partidos, self.facturas)
                md.menu()

            elif opcion == 6:
                md = Modulo6(self.equipos, self.estadios, self.partidos, self.facturas)
                md.menu()

            elif opcion == 7:
                limpiar()
                print("Los cambios se han guardado exitosamente!")
                self.guardarDatos()
                salir()

            elif opcion == 8:
                run = False

            elif opcion == 9:
                with open("Datos\equipos.txt", 'w') as archivo:
                    pass
                with open("Datos\equipos.txt", 'w') as archivo:
                    pass
                with open("Datos\partidos.txt", 'w') as archivo:
                    pass
                self.cargarDatos()


            