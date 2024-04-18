import mysql.connector
import usuarioModel
from utils import connector

def extraeUsuarios():
    # Establecer la conexión
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    # Ejemplo de consulta
    cursor.execute("SELECT * FROM usuario")
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
    conexion = connector.dbConnection()
    cursor = conexion.cursor()
    # Ejemplo de consulta
    cursor.execute(f"SELECT * FROM usuario WHERE id_usuario = {codigo}")
    usuarios = []
    # Obtener los resultados
    resultados = cursor.fetchone()
    usuario = usuarioModel.asignarDatos(resultados)
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    return usuario

datosUsuario = extraeUsuarios()
print(datosUsuario)
datosUsuario = extraeUsuario(1)
print(datosUsuario)
