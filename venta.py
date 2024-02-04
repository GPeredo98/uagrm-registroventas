from almacen import Almacen
from cliente import Cliente
from condicion_pago import CondicionPago
from producto import Producto
from venta_detalle import VentaDetalle

class Venta:
    def __init__(self, codigo_venta, cliente, descuento, almacen, condicion_pago, tipo_venta, tipo_entrega):
        self.codigo_venta = codigo_venta
        self.cliente = cliente
        self.descuento = descuento
        self.almacen = almacen
        self.condicion_pago = condicion_pago
        self.tipo_venta = tipo_venta
        self.tipo_entrega = tipo_entrega
        self.detalles_venta = []

    def agregar_venta_detalle(self, producto, cantidad, descuento):
        detalle = VentaDetalle(self.codigo_venta, producto['codigo_producto'], producto['nombre_producto'], producto['precio_unitario'], cantidad, descuento)
        self.detalles_venta.append(detalle)
        print(f"Producto {producto['nombre_producto']} agregado a la venta {self.codigo_venta}.")

    def calcular_total(self):
        total = sum(detalle.calcular_subtotal() for detalle in self.detalles_venta)
        total -= total * (self.descuento / 100)
        return total

    def grabar_venta(self):
        ventas_temporales.append(self)
        for detalle in self.detalles_venta:
            detalle.grabar_venta_detalle()  # Llamada al método para grabar el detalle
        print(f"Venta {self.codigo_venta} grabada correctamente.")

    @staticmethod
    def listar_ventas():
        return ventas_temporales

    @staticmethod
    def registrar_venta(codigo_venta, cliente, descuento, almacen, condicion_pago, tipo_venta, tipo_entrega):
        nueva_venta = Venta(codigo_venta, cliente, descuento, almacen, condicion_pago, tipo_venta, tipo_entrega)
        ventas_temporales.append(nueva_venta)
        return nueva_venta

    def to_dict(self):
        return {
            'codigo_venta': self.codigo_venta,
            'cliente': self.cliente.to_dict(),
            'descuento': self.descuento,
            'almacen': self.almacen.to_dict(),
            'condicion_pago': self.condicion_pago.to_dict(),
            'tipo_venta': self.tipo_venta,
            'tipo_entrega': self.tipo_entrega
        }
    def listar_ventas_detalle(self):
        return [detalle.to_dict() for detalle in self.detalles_venta]

    @staticmethod
    def obtener_venta_por_codigo(codigo_venta):
        return next((venta for venta in ventas_temporales if venta.codigo_venta == codigo_venta), None)

# Lista temporal para simular el almacenamiento
ventas_temporales = []
