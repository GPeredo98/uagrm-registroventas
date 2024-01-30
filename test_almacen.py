from almacen import Almacen

def test_registrar_almacen():
    almacen = Almacen("A001", "Almacen001")
    almacen.grabar_almacen()

    assert len(Almacen.listar_almacenes()) == 1