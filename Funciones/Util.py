import requests
import pickle
import math
from Clases.Equipo import Equipo
from Clases.Estadio import Estadio
from Clases.Partido import Partido
from Clases.Producto import Producto
from Clases.Restaurante import Restaurante
from os import system

"""Funcion para validar numero enteros"""
def input_int(string):
    valor = input(string)
    while not valor.isnumeric():
        valor = input(f"Error: {string}")
    return int(valor)

"""Funcion para validar strings (Sin numeros)"""
def input_str(string):
    valor = input(string)
    while valor.isnumeric():
        valor = input(f"Error: {string}")
    return valor


"""Funcion para validar la entrada de opciones"""
def input_opciones(num_opciones, string="Ingrese el numero de la opcion deseada: "):
    valor = input(string)
    while not valor.isnumeric() or int(valor) not in range(1, int(num_opciones)+1):
        valor = input(f"Error: {string}")
    return int(valor)


"""Funcion para validar la entrada de un dia"""
def input_dia(string="Ingrese dia: "):
    valor = input(string)
    while not valor.isnumeric() or int(valor) not in range(1, 31):
        valor = input(f"Error: {string}")
    return int(valor)


"""Funcion para validar la entrada de un mes"""
def input_mes(string="Ingrese mes: "):
    valor = input(string)
    while not valor.isnumeric() or int(valor) not in range(1, 12):
        valor = input(f"Error: {string}")
    return int(valor) 


"""Funcion para validar la entrada de un año"""
def input_año(string="Ingrese año: "):
    valor = input(string)
    while not valor.isnumeric() or int(valor) < 0:
        valor = input(f"Error: {string}")
    return int(valor)


"""Funcion para obtener los datos de una api"""
def consumir_API(url):
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        dato = respuesta.json()  
        return dato

    else:
        print(f"Error: {respuesta.status_code}")


"""Funcion para guardar datos en un txt usando pickle"""
def guardar_txt(ruta, datos):
    with open(ruta, 'wb') as archivo:
        pickle.dump(datos, archivo)       


"""Funcion para limpiar la terminal"""
def limpiar():
    system("cls")
    system("cls")
    system("cls")


"""Funcion para salir de un apartado de la app"""
def salir():
    input("Presione enter para salir...")

"""Funcion para cargar los datos de los equipos de la api"""
def cargarEquipos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    equipos_api = consumir_API(url)
    equipos = []


    for equipo in equipos_api:
        equipos.append(
            Equipo(
                equipo["id"],
                equipo["code"],
                equipo["name"],
                equipo["group"]
            )
        )
    
    return equipos


"""Funcion para cargar los datos de los estadios de la api"""
def cargarEstadios():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    estadios_api = consumir_API(url)
    estadios = []
  

    for estadio in estadios_api:        
        id = estadio["id"]
        nombre_estadio = estadio["name"]
        ciudad = estadio["city"]
        capacidad = estadio["capacity"]
        restaurantes_json = estadio["restaurants"]

        estadio_objeto = Estadio(id, nombre_estadio, ciudad, capacidad)

        for restaurante in restaurantes_json:
            nombre_restaurante = restaurante["name"]
            productos_json = restaurante["products"]
            
            restaurante_objeto = Restaurante(nombre_restaurante)

            for producto in productos_json:
                nombre_producto = producto["name"]
                cantidad = producto["quantity"]
                precio = producto["price"]
                stock = producto["stock"]
                adicional = producto["adicional"]

                restaurante_objeto.productos.append(
                    Producto(nombre_producto, cantidad, precio, stock, adicional)    
                )
            
            estadio_objeto.restaurantes.append(
                restaurante_objeto
            )
                
        estadios.append(estadio_objeto)

    return estadios


"""Funcion para cargar los partidos de la api"""
def cargarPartidos(estadios):
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"

    partidos_api = consumir_API(url)
    partidos = []


    for partido in partidos_api:
        for estadio in estadios:

            if estadio.id == partido["stadium_id"]:
                estadio_partido = estadio

        asientos_general = []
        filas = math.ceil(estadio_partido.capacidad[0] / 10)
        asientos_restantes = estadio_partido.capacidad[0] 
        for _ in range(filas):
            fila_asientos = []
            for _ in range(min(10, asientos_restantes)):
                fila_asientos.append([" "])
            asientos_general.append(fila_asientos)
            asientos_restantes -= len(fila_asientos)

            
        asientos_vip = []
        filas = math.ceil(estadio_partido.capacidad[1] / 10)
        asientos_restantes = estadio_partido.capacidad[1] 
        for _ in range(filas):
            fila_asientos = []
            for _ in range(min(10, asientos_restantes)):
                fila_asientos.append([" "])
            asientos_vip.append(fila_asientos)
            asientos_restantes -= len(fila_asientos)

        partido_objeto = Partido(
            partido["id"],
            partido["number"],
            partido["home"]["id"],
            partido["away"]["id"],
            partido["date"],
            partido["group"],
            partido["stadium_id"],
            asientos_general,
            asientos_vip
        )

        partidos.append(partido_objeto)
    
    return partidos


"""Funcion para saber si un numero de vapiro"""
def es_vampiro(numero):
    str_numero = str(numero)
    longitud = len(str_numero)
    
    if longitud % 2 != 0:
        return False
    
    mitad = longitud // 2
    
    for i in range(10**(mitad - 1), 10**mitad):
        for j in range(i, 10**mitad):
            if i * j == numero:
                colmillos = str(i) + str(j)
                if sorted(str_numero) == sorted(colmillos):
                    return True
    
    return False

"""Funcion para saber si un numero es perfecto"""
def es_numero_perfecto(numero):
    if numero <= 1:
        return False

    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    
    return suma_divisores == numero
    





    

    




        





