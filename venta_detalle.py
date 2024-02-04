# ...

class VentaDetalle:
    def __init__(self, codigo_venta, codigo_producto, nombre_producto, precio_unitario, cantidad, descuento):
        self.codigo_venta = codigo_venta
        self.codigo_producto = codigo_producto
        self.nombre_producto = nombre_producto
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descuento = descuento

    def calcular_subtotal(self):
        subtotal = self.precio_unitario * self.cantidad
        subtotal -= subtotal * (self.descuento / 100)  # Aplicar descuento de detalle si existe
        return subtotal

    def grabar_venta_detalle(self):
        detalles_ventas_temporales.append(self)
        print(f"Detalle de venta para el producto {self.nombre_producto} grabado correctamente.")

    @staticmethod
    def listar_detalles_ventas():
        return detalles_ventas_temporales
    
    @staticmethod
    def listar_detalles_venta_por_codigo(codigo_venta):
        return [detalle.to_dict() for detalle in detalles_ventas_temporales if detalle.codigo_venta == codigo_venta]

    def to_dict(self):
        return {
            'codigo_venta': self.codigo_venta,
            'codigo_producto': self.codigo_producto,
            'nombre_producto': self.nombre_producto,
            'precio_unitario': self.precio_unitario,
            'cantidad': self.cantidad,
            'descuento': self.descuento
        }

# Lista temporal para simular el almacenamiento de detalles de ventas
detalles_ventas_temporales = []
