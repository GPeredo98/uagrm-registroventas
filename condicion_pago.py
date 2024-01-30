class CondicionPago:
    def __init__(self, codigo_condicion_pago, descripcion_condicion_pago):
        self.codigo_condicion_pago = codigo_condicion_pago
        self.descripcion_condicion_pago = descripcion_condicion_pago

    def grabar_condicion_pago(self):
        # Agregar lógica para grabar la condición de pago en tu sistema o base de datos
        condiciones_pago_temporales.append(self)
        print(f"Condición de pago {self.descripcion_condicion_pago} grabada correctamente.")

    @staticmethod
    def listar_condiciones_pago():
        # Devolver la lista de condiciones de pago almacenadas
        return condiciones_pago_temporales

# Lista temporal para simular el almacenamiento
condiciones_pago_temporales = []
