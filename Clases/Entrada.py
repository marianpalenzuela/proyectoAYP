import uuid 

"""
Clase Entrada (Boleto)
"""

class Entrada:
    
    """Constructor"""

    def __init__(self, nombre, cedula, edad, tipo, total, fila, columna) -> None:
        self.codigo = str(uuid.uuid4())
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo = tipo
        self.total = total
        self.fila = fila
        self.columna = columna
        self.asistencia = False

    """Metodo para enseñar la informacion de la clase"""

    def mostrarInfo(self):
        if self.tipo == 1:
            tipo = "General"
        elif self.tipo == 2:
            tipo = "VIP"

        print(f"""
        Codigo: {self.codigo}
        Nombre: {self.nombre}
        Cedula: {self.cedula}
        Edad: {self.edad}
        Tipo: {tipo}
        Total: {self.total}$
        Fila: {self.fila}
        Columna: {self.columna}
        Asistencia: {self.asistencia}
        """)