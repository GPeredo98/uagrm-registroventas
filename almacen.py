class Almacen:
    def __init__(self, codigo_almacen, nombre_almacen):
        self.codigo_almacen = codigo_almacen
        self.nombre_almacen = nombre_almacen

    def grabar_almacen(self):
        # Agregar lógica para grabar el almacén en tu sistema o base de datos
        almacenes_temporales.append(self)
        print(f"Almacén {self.nombre_almacen} grabado correctamente.")

    @staticmethod
    def listar_almacenes():
        # Devolver la lista de almacenes almacenados
        return almacenes_temporales

# Lista temporal para simular el almacenamiento
almacenes_temporales = []
