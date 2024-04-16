import mysql.connector
import usuarioModel

# Establecer la conexión
conexion = mysql.connector.connect(
    host="148.202.39.38",  # Cambia esto al host de tu base de datos MySQL
    user="test",    # Cambia esto al nombre de usuario de tu base de datos
    password="test",  # Cambia esto a la contraseña de tu base de datos
    database="mercadocucea"  # Cambia esto al nombre de tu base de datos
)

# Comprobar si la conexión se estableció correctamente
if conexion.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

# Realizar operaciones en la base de datos
cursor = conexion.cursor()

# Ejemplo de consulta
cursor.execute("SELECT * FROM usuario")

usuario1 = usuarioModel.usuario

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila[3])

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
