from condicion_pago import CondicionPago

def test_registrar_condicion_pago():
    condicion_pago = CondicionPago("CP001", "Condicion de Pago 001")
    condicion_pago.grabar_condicion_pago()

    assert len(CondicionPago.listar_condiciones_pago()) == 1