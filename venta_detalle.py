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
