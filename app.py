import json
from flask import Flask, jsonify, request
from cliente import Cliente
from almacen import Almacen
from producto import Producto
from condicion_pago import CondicionPago
from venta import Venta

app = Flask(__name__)

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

@app.route('/api/clientes', methods=['POST'])
def guardar_cliente():
    data = request.json
    cliente = Cliente(data['codigo_cliente'], data['nombre_cliente'])
    cliente.grabar_cliente()
    return jsonify(True)

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

@app.route('/api/ventas', methods=['POST'])
def crear_venta():
    data = request.get_json()
    codigo_venta = data.get('codigo_venta')
    codigo_cliente = data.get('codigo_cliente')
    descuento = float(data.get('descuento', 0.0))
    codigo_almacen = data.get('codigo_almacen')
    codigo_condicion_pago = data.get('codigo_condicion_pago')

    cliente = next((c for c in Cliente.listar_clientes() if c.codigo_cliente == codigo_cliente), None)
    almacen = next((a for a in Almacen.listar_almacenes() if a.codigo_almacen == codigo_almacen), None)
    condicion_pago = next((cp for cp in CondicionPago.listar_condiciones_pago() if cp.codigo_condicion_pago == codigo_condicion_pago), None)

    if cliente and almacen and condicion_pago:
        nueva_venta = Venta.registrar_venta(codigo_venta, cliente, descuento, almacen, condicion_pago)
        return jsonify(nueva_venta.__dict__)
    else:
        return jsonify({'error': 'Cliente, almacén o condición de pago no encontrados'}), 400

if __name__ == '__main__':
    app.run(debug=True)
