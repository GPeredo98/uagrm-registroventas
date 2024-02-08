from behave import *
from producto import Producto
from venta import Venta
from cliente import Cliente
from almacen import Almacen
from condicion_pago import CondicionPago

@given(
    'se agrega al carrito item(s) con codigo "{cod_producto}", nombre "{nombre}", en la cantidad de {cantidad:d} unidades, al precio unitario de {precio_unitario:f} y con un descuento del {descuento:d}%')
def step_definir_producto(context, cod_producto, nombre, cantidad, precio_unitario, descuento):
    context.producto = {
        "codProducto": cod_producto,
        "producto": nombre,
        "precioUnitario": precio_unitario,
        "cantidad": cantidad,
        "descuento": descuento
    }
    print("")
    print("Paso GIVEN>")
    producto = Producto(cod_producto, nombre, cantidad, precio_unitario, descuento)
    producto.grabar_producto()
    print("Producto seleccionado correctamente.............")
    print(f"Codigo del Producto: {producto.codigo_producto}, Producto: {producto.nombre_producto}, Precio: {producto.precio_unitario}, Cantidad: {producto.cantidad_producto}, Descuento: {producto.porcentaje_descuento}")

@when("se verifica el producto")
def step_agregar_al_carrito(context):
    item = context.producto
    print("")
    print("Paso WHEN>")
    print("Producto agregado correctamente.............")
    print(f"Producto {item["producto"]} agregado al carrito")

@then('el producto debe estar en el carrito con un precio de {precio_total:f}')
def step_verificar_carrito(context, precio_total):
    print("")
    print("Paso THEN>")
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()
    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()
    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()
    items = len(Producto.listar_productos())
    producto1 = Producto.listar_productos()[items-1]
    venta = Venta.registrar_venta("V001", cliente, 0.0, almacen, condicion_pago, "PRODUCTO", "En Tienda")
    venta.agregar_venta_detalle(producto1, producto1.cantidad_producto, producto1.porcentaje_descuento)
    assert Venta.calcular_total(venta) == precio_total, f"El Precio esperado era: {precio_total} y se consiguio: {Venta.calcular_total(venta)}"