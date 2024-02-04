import requests

# URL de la API
url_guardar_almacen = 'http://localhost:5000/api/almacenes'

# Datos para el almacén que deseas guardar
datos_almacen = {
    'codigo': 'A005',
    'nombre': 'Almacén de Ejemplo'
}

# Realizar la solicitud POST
response = requests.post(url_guardar_almacen, json=datos_almacen)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    print("Almacén guardado exitosamente.")
else:
    print(f"Error al guardar el almacén. Código de respuesta: {response.status_code}")
    print(response.text)  # Imprimir el contenido de la respuesta en caso de error
