from cliente import Cliente
from almacen import Almacen
from producto import Producto
from condicion_pago import CondicionPago
from venta import Venta
from venta_detalle import VentaDetalle

class PruebaVenta:
    @staticmethod
    def ejecutar_prueba():
        # Agregar algunos clientes, almacenes y productos
        Cliente("C001", "Cliente1").grabar_cliente()
        Almacen("A001", "Almacen1").grabar_almacen()
        Producto("P001", "Producto1", 10.0, 0.0).grabar_producto()
        Producto("P002", "Producto2", 20.0, 5.0).grabar_producto()
        Producto("S001", "Servicio1", 100.0, 2.0).grabar_producto()

        # Listar productos
        print("\nListado de Productos:")
        for producto in Producto.listar_productos():
            print(f"Código: {producto.codigo_producto}, Nombre: {producto.nombre_producto}, Precio: {producto.precio_unitario}")

        # Crear una venta
        venta = Venta.registrar_venta("V001", Cliente.listar_clientes()[0], 5.0, Almacen.listar_almacenes()[0],
                                      CondicionPago("CP001", "Contado"), "PRODUCTO")

        # Agregar productos a la venta
        producto1 = Producto.listar_productos()[0]
        producto2 = Producto.listar_productos()[1]

        venta.agregar_venta_detalle(producto1, 2, 0)
        venta.agregar_venta_detalle(producto2, 1, 0)

        # Mostrar detalles de la venta
        print("\nDetalles de la Venta:")
        for detalle in venta.detalles_venta:
            print(f"Producto: {detalle.nombre_producto}, Cantidad: {detalle.cantidad}, Subtotal: {detalle.calcular_subtotal()}")

        # Calcular y mostrar el total de la venta
        total_venta = venta.calcular_total()
        print(f"\nTotal de la Venta: {total_venta}")

        # Grabar la venta
        venta.grabar_venta()

        # Listar ventas almacenadas
        print("\nVentas Almacenadas:")
        for v in Venta.listar_ventas():
            print(f"Código: {v.codigo_venta}, Total: {v.calcular_total()}")

        # Quitar un producto
        Producto.quitar_producto("P002")

        # Listar productos actualizados
        print("\nProductos Actualizados:")
        for p in Producto.listar_productos():
            print(f"Código: {p.codigo_producto}, Nombre: {p.nombre_producto}, Precio: {p.precio_unitario}")


# Ejecutar la prueba
PruebaVenta.ejecutar_prueba()
