class Producto:
    def __init__(self, codigo_producto, nombre_producto, precio_unitario, porcentaje_descuento):
        self.codigo_producto = codigo_producto
        self.nombre_producto = nombre_producto
        self.precio_unitario = precio_unitario
        self.porcentaje_descuento = porcentaje_descuento

    def grabar_producto(self):
        productos_temporales.append(self)
        print(f"Producto {self.nombre_producto} grabado correctamente.")

    @staticmethod
    def listar_productos():
        return productos_temporales

    @staticmethod
    def agregar_producto(producto):
        productos_temporales.append(producto)
        print(f"Producto {producto.nombre_producto} agregado correctamente.")

    @staticmethod
    def quitar_producto(codigo_producto):
        producto = next((p for p in productos_temporales if p.codigo_producto == codigo_producto), None)
        if producto:
            productos_temporales.remove(producto)
            print(f"Producto {producto.nombre_producto} eliminado correctamente.")
        else:
            print(f"Producto con código {codigo_producto} no encontrado.")

# Lista temporal para simular el almacenamiento
productos_temporales = []
