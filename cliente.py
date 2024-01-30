class Cliente:
    def __init__(self, codigo_cliente, nombre_cliente):
        self.codigo_cliente = codigo_cliente
        self.nombre_cliente = nombre_cliente

    def grabar_cliente(self):
        # Aquí, puedes asumir que se está almacenando en una lista temporal
        clientes_temporales.append(self)
        print(f"Cliente {self.nombre_cliente} grabado correctamente.")

    @staticmethod
    def listar_clientes():
        # Devolver la lista de clientes almacenados
        return clientes_temporales
    
    def to_dict(self):
        return {
            'codigo_cliente': self.codigo_cliente,
            'nombre_cliente': self.nombre_cliente,
        }

# Lista temporal para simular el almacenamiento
clientes_temporales = []
cliente1 = Cliente("C001", "Cliente1")
cliente1.grabar_cliente()
cliente2 = Cliente("C002", "Cliente2")
cliente2.grabar_cliente()