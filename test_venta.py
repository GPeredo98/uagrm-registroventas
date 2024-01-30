from cliente import Cliente
from almacen import Almacen
from condicion_pago import CondicionPago
from venta import Venta
from producto import Producto


###############################################
# Test para Registrar una Venta de un Producto
###############################################
def test_registrar_venta_producto():
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()

    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()

    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()

    producto = Producto("P001", "Producto 01", 20.00, 2.0)
    producto.grabar_producto()

    venta = Venta.registrar_venta("V001", cliente, 5.0, almacen, condicion_pago, "PRODUCTO")
    venta.agregar_venta_detalle(producto, 2, 5.0)

    assert len(Venta.listar_ventas()) == 1


###############################################
# Test para Registrar una Venta de un Servicio
###############################################
def test_registrar_venta_servicio():
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()

    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()

    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()

    producto = Producto("S001", "Servicio 01", 100.00, 0.0)
    producto.grabar_producto()

    venta = Venta.registrar_venta("V001", cliente, 5.0, almacen, condicion_pago, "SERVICIO")
    venta.agregar_venta_detalle(producto, 100, 0.0)

    assert len(Venta.listar_ventas()) == 1 


##########################################################################
# Test para Calcular el total de la venta aplicando descuento al producto
###########################################################################
def test_calcular_total_venta_descuento_producto():
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()

    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()

    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()

    #Registramos 3 productos
    producto1 = Producto("P001", "Producto 01", 50.00, 10.0)
    producto1.grabar_producto()

    producto2 = Producto("P002", "Producto 02", 100.00, 10.0)
    producto2.grabar_producto()

    producto3 = Producto("P003", "Producto 03", 10.00, 10.0)
    producto3.grabar_producto()

    venta = Venta.registrar_venta("V001", cliente, 0.0, almacen, condicion_pago, "PRODUCTO")
    venta.agregar_venta_detalle(producto1, 1, 10.0)
    venta.agregar_venta_detalle(producto2, 1, 5.0)
    venta.agregar_venta_detalle(producto3, 1, 0.0)

    assert Venta.calcular_total(venta) == 150


######################################################################
# Test para Calcular el total de la venta aplicando descuento global
######################################################################
def test_calcular_total_venta_descuento_global():
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()

    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()

    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()

    #Registramos 3 productos
    producto1 = Producto("P001", "Producto 01", 50.00, 10.0)
    producto1.grabar_producto()

    producto2 = Producto("P002", "Producto 02", 100.00, 10.0)
    producto2.grabar_producto()

    producto3 = Producto("P003", "Producto 03", 10.00, 10.0)
    producto3.grabar_producto()

    venta = Venta.registrar_venta("V001", cliente, 10.0, almacen, condicion_pago, "PRODUCTO")
    venta.agregar_venta_detalle(producto1, 1, 0.0)
    venta.agregar_venta_detalle(producto2, 1, 0.0)
    venta.agregar_venta_detalle(producto3, 1, 0.0)

    assert Venta.calcular_total(venta) == 144