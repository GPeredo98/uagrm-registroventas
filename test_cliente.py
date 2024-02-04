from cliente import Cliente

def test_registrar_cliente():
    cliente = Cliente("C001", "Cliente001")
    cliente.grabar_cliente()

    assert len(Cliente.listar_clientes()) == 1