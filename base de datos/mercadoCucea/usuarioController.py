import mysql.connector
import usuarioModel
from utils import connector

def extraeUsuarios():
    # Establecer la conexión
    cursor= connector.dbConnection()
    # Ejemplo de consulta
    cursor.execute("SELECT * FROM usuario WHERE id_usuario")
    usuarios = []
    # Obtener los resultados
    resultados = cursor.fetchall()
    # Imprimir los resultados
    for fila in resultados:
        usuario = usuarioModel.asignarDatos(fila)
        usuarios.append(usuario)
    # Cerrar el cursor y la conexión
    return usuarios

def extraeUsuario(codigo):
    # Establecer la conexión
    conexion = mysql.connector.connect(
        host="148.202.39.38",  # Cambia esto al host de tu base de datos MySQL
        user="test",    # Cambia esto al nombre de usuario de tu base de datos
        password="test",  # Cambia esto a la contraseña de tu base de datos
        database="mercadocucea"  # Cambia esto al nombre de tu base de datos
    )
    # Realizar operaciones en la base de datos
    cursor = conexion.cursor()
    # Ejemplo de consulta
    cursor.execute(f"SELECT * FROM usuario WHERE id_usuario = {codigo}")
    usuarios = []
    # Obtener los resultados
    resultados = cursor.fetchall()
    # Imprimir los resultados
    for fila in resultados:
        usuario1 = usuarioModel.usuario
        usuario1['id_usuario']=fila[0]
        usuario1['usuario']=fila[1]
        usuario1['correo']=fila[3]
        usuario1['nombre']=fila[4]
        usuario1['apellidoPaterno']=fila[5]
        usuario1['apellidoMaterno']=fila[6]
        usuario1['puesto']=fila[7]
        usuario1['telefono']=fila[8]
        usuarios.append(usuario1)
        del usuario1
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    return usuarios

datosUsuario = extraeUsuarios()
print(datosUsuario)
datosUsuario = extraeUsuario(2)
print(datosUsuario)