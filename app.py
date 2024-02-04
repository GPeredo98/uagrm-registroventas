import json
from flask import Flask, jsonify, request
from cliente import Cliente
from almacen import Almacen
from producto import Producto
from condicion_pago import CondicionPago
from venta import Venta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/condiciones_pago', methods=['GET'])
def obtener_cpagos():
    pagos = [condicion_pago.__dict__ for condicion_pago in CondicionPago.listar_condiciones_pago()]
    return jsonify(pagos)

@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    clientes = [cliente.__dict__ for cliente in Cliente.listar_clientes()]
    return jsonify(clientes)

@app.route('/api/almacenes', methods=['GET'])
def obtener_almacenes():
    almacenes = [almacen.__dict__ for almacen in Almacen.listar_almacenes()]
    return jsonify(almacenes)

@app.route('/api/almacenes', methods=['POST'])
def guadar_almacen():
    data = request.json
    almacen = Almacen(data['codigo'], data['nombre'])
    almacen.grabar_almacen()
    return jsonify(True)

# ...

@app.route('/api/clientes', methods=['POST'])
def guardar_cliente():
    data = request.json
    codigo_cliente = data['codigo_cliente']
    nombre_cliente = data['nombre_cliente']
    numero_ci_nit = data['numero_ci_nit']
    tipo_documento = data['tipo_documento']
    email = data['email']

    cliente = Cliente(codigo_cliente, nombre_cliente, numero_ci_nit, tipo_documento, email)
    cliente.grabar_cliente()
    return jsonify(True)

# ...


@app.route('/api/condiciones_pago', methods=['POST'])
def guardar_condicion_pago():
    data = request.json
    condicion_pago = CondicionPago(data['codigo_condicion_pago'], data['descripcion'])
    condicion_pago.grabar_condicion_pago()
    return jsonify(True)

@app.route('/api/productos', methods=['POST'])
def guardar_producto():
    data = request.json
    producto = Producto(data['codigo_producto'], data['nombre_producto'], data['precio_unitario'], data['porcentaje_descuento'])
    producto.grabar_producto()
    return jsonify(True)

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = [producto.__dict__ for producto in Producto.listar_productos()]
    return jsonify(productos)

@app.route('/api/ventas', methods=['GET'])
def obtener_ventas():
    ventas = [venta.to_dict() for venta in Venta.listar_ventas()]
    return jsonify(ventas)





# ...

@app.route('/api/ventas', methods=['POST'])
def crear_venta():
    data = request.get_json()
    codigo_venta = data.get('codigo_venta')
    codigo_cliente = data.get('codigo_cliente')
    descuento = float(data.get('descuento', 0.0))
    codigo_almacen = data.get('codigo_almacen')
    codigo_condicion_pago = data.get('codigo_condicion_pago')
    tipo_venta = data.get('tipo_venta')
    tipo_entrega = data.get('tipo_entrega')
    productos = data.get('productos')

    cliente = next((c for c in Cliente.listar_clientes() if c.codigo_cliente == codigo_cliente), None)
    almacen = next((a for a in Almacen.listar_almacenes() if a.codigo_almacen == codigo_almacen), None)
    condicion_pago = next((cp for cp in CondicionPago.listar_condiciones_pago() if cp.codigo_condicion_pago == codigo_condicion_pago), None)

    if cliente and almacen and condicion_pago:
        nueva_venta = Venta.registrar_venta(codigo_venta, cliente, descuento, almacen, condicion_pago, tipo_venta, tipo_entrega)
        for producto in productos:
            nueva_venta.agregar_venta_detalle(producto, producto['cantidad'], producto['descuento'])

        return jsonify(True)
    else:
        return jsonify({'error': 'Cliente, almacén o condición de pago no encontrados'}), 400

# ...
# ...

@app.route('/api/ventas/<codigo_venta>/detalles', methods=['GET'])
def obtener_detalles_venta(codigo_venta):
    venta = Venta.obtener_venta_por_codigo(codigo_venta)
    if venta:
        detalles_venta = venta.listar_ventas_detalle()
        return jsonify(detalles_venta)
    else:
        return jsonify({'error': 'Venta no encontrada'}), 404

@app.route('/api/ventas/detalles', methods=['GET'])
def obtener_todas_ventas_detalles():
    detalles_venta = [detalle.to_dict() for venta in Venta.listar_ventas() for detalle in venta.detalles_venta]
    return jsonify(detalles_venta)

# ...


    

if __name__ == '__main__':
    app.run(debug=True)
