class Equipo:

    """Constructor"""

    def __init__(self, id, codigo, nombre, grupo) -> None:
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.grupo = grupo


    """Metodo para enseñar la informacion de la clase"""
    
    def mostrarInfo(self):
        print(f"""
        ID: {self.id}
        Codigo: {self.codigo}
        Nombre: {self.nombre}
        Grupo: {self.grupo}
        """)